$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$problemDir = Split-Path -Parent $PSScriptRoot
& "C:\Users\Charlie Yu\Documents\Bitbucket - cyuconsulting\leetcode-solutions\scripts\test-problem.ps1" -Folder "1430_check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree" -Language "python"
