$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$problemDir = Split-Path -Parent $PSScriptRoot
& "C:\Users\Charlie Yu\Documents\Bitbucket - cyuconsulting\leetcode-solutions\scripts\test-problem.ps1" -Folder "2584_split_the_array_to_make_coprime_products" -Language "go"
