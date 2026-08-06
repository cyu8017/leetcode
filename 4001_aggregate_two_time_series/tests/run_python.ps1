$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
& "C:\Users\Charlie Yu\Documents\leetcode\scripts\test.ps1" -Folder "4001_aggregate_two_time_series" -Language "python"
