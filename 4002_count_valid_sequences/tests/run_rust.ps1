$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
& "C:\Users\Charlie Yu\Documents\leetcode\scripts\test.ps1" -Folder "4002_count_valid_sequences" -Language "rust"
