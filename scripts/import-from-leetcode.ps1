param(
    [string]$Folder = "",
    [int]$Number = 0,
    [switch]$All,
    [switch]$AllLanguages,
    [string]$Language = "",
    [int]$Limit = 0,
    [switch]$Overwrite,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "import-from-leetcode.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($Folder) { $args += @("--folder", $Folder) }
if ($Number -gt 0) { $args += @("--number", $Number) }
if ($All) { $args += "--all" }
if ($AllLanguages) { $args += "--all-languages" }
if ($Language) { $args += @("--language", $Language) }
if ($Limit -gt 0) { $args += @("--limit", $Limit) }
if ($Overwrite) { $args += "--overwrite" }
if ($DryRun) { $args += "--dry-run" }

python @args
