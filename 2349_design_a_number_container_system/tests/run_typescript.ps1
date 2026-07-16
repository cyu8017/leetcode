$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$problemDir = Split-Path -Parent $PSScriptRoot
& "C:\Users\Charlie Yu\Documents\Bitbucket - cyuconsulting\leetcode-solutions\scripts\test-problem.ps1" -Folder "2349_design_a_number_container_system" -Language "typescript"
