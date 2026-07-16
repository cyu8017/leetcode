param(
    [int]$Number = 0,
    [switch]$Force,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "sync-test-config.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($Number -gt 0) { $args += @("--number", $Number) }
if ($Force) { $args += "--force" }
if ($DryRun) { $args += "--dry-run" }

python @args
