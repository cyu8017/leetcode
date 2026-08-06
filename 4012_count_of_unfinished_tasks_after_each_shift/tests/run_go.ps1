$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
& "C:\Users\Charlie Yu\Documents\leetcode\scripts\test.ps1" -Folder "4012_count_of_unfinished_tasks_after_each_shift" -Language "go"
