param(
    [switch]$Local,
    [switch]$FailFast
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "run-smoke.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($Local) { $args += "--local" }
if ($FailFast) { $args += "--fail-fast" }

python @args
exit $LASTEXITCODE
