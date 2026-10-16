# PowerShell wrapper for genuine simulator screenshot capture
param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2")]
    [string]$Program,

    [int]$Delay = 2
)

python "$PSScriptRoot\capture_evidence.py" --program $Program --delay $Delay
