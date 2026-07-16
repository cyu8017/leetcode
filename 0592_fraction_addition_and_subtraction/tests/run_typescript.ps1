$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$problemDir = Split-Path -Parent $PSScriptRoot
& "C:\Users\Charlie Yu\Documents\Bitbucket - cyuconsulting\leetcode-solutions\scripts\test-problem.ps1" -Folder "0592_fraction_addition_and_subtraction" -Language "typescript"
