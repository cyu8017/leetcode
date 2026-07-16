$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$problemDir = Split-Path -Parent $PSScriptRoot
& "C:\Users\Charlie Yu\Documents\Bitbucket - cyuconsulting\leetcode-solutions\scripts\test-problem.ps1" -Folder "2510_check_if_there_is_a_path_with_equal_number_of_0s_and_1s" -Language "typescript"
