param(
    [string[]]$Language = @(),
    [switch]$Local,
    [switch]$FailFast,
    [string]$Folder = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "run-solved.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($Local) { $args += "--local" }
if ($FailFast) { $args += "--fail-fast" }
if ($Folder) { $args += @("--folder", $Folder) }
foreach ($lang in $Language) {
    $args += @("--language", $lang)
}

python @args
