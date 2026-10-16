# Experiment 1 - File Inventory & Integrity Manifest Script
# Safe read-only inspection tool

param (
    [string]$RootPath = "$PSScriptRoot\..\..",
    [string]$OutputPath = "$PSScriptRoot\..\Logs\file_manifest.json"
)

$ErrorActionPreference = "Stop"

Write-Host "Scanning directory: $RootPath"

# Collect all files under root and Experiment_1
$files = Get-ChildItem -Path $RootPath -Recurse -File -Force | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and $_.FullName -notmatch '\\scratch\\'
}

$manifest = @()

foreach ($file in $files) {
    try {
        # Calculate SHA256 using safe file sharing mode
        $fileStream = [System.IO.File]::Open($file.FullName, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::ReadWrite)
        $sha = [System.Security.Cryptography.SHA256]::Create()
        $hashBytes = $sha.ComputeHash($fileStream)
        $hash = [System.BitConverter]::ToString($hashBytes) -replace '-'
        $fileStream.Close()

        $relPath = $file.FullName.Substring((Resolve-Path $RootPath).Path.Length).TrimStart('\', '/')

        $manifest += [PSCustomObject]@{
            RelativePath   = $relPath
            Name           = $file.Name
            Extension      = $file.Extension
            SizeBytes      = $file.Length
            LastModified   = $file.LastWriteTime.ToString("o")
            SHA256         = $hash
            IsOriginal     = -not ($relPath.StartsWith("Experiment_1\"))
        }
    } catch {
        Write-Warning "Could not process file $($file.FullName): $_"
    }
}

$jsonOutput = $manifest | ConvertTo-Json -Depth 5
$outputDir = Split-Path $OutputPath -Parent
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

[System.IO.File]::WriteAllText((Resolve-Path -Path $outputDir).Path + "\" + (Split-Path $OutputPath -Leaf), $jsonOutput, [System.Text.Encoding]::UTF8)

# Also output a clean summary table to console
Write-Host "`n=== FILE INVENTORY MANIFEST ($($manifest.Count) files) ===" -ForegroundColor Cyan
$manifest | Format-Table RelativePath, SizeBytes, LastModified, SHA256 -AutoSize

Write-Host "`nManifest written to: $OutputPath" -ForegroundColor Green
