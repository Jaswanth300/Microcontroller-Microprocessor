# PowerShell wrapper for program comparison
param ()
python "$PSScriptRoot\compare_programs.py"
Get-Content "$PSScriptRoot\..\Logs\duplicate_analysis_report.md"
