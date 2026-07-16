$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
& "C:\Users\Charlie Yu\Documents\Bitbucket - cyuconsulting\leetcode-solutions\scripts\test.ps1" -Folder "3991_sort_array_using_prefix_reversals" -Language "c"
