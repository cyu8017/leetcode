param(
    [switch]$Force,
    [switch]$ForceRefresh,
    [switch]$DryRun,
    [int]$Number = 0
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "sync-test-cases.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($Force) { $args += "--force" }
if ($ForceRefresh) { $args += "--force-refresh" }
if ($DryRun) { $args += "--dry-run" }
if ($Number -gt 0) { $args += @("--number", $Number) }

python @args
