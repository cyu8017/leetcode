param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "sync-test-cases.py"
$args = @(
    $pythonScript,
    "--repo-root", $repoRoot,
    "--tag", "database",
    "--legacy-sql-only",
    "--force"
)
if ($DryRun) { $args += "--dry-run" }

python @args

if (-not $DryRun) {
    python (Join-Path $PSScriptRoot "sync-test-config.py") --repo-root $repoRoot --force
    python (Join-Path $PSScriptRoot "validate-repo.py") --repo-root $repoRoot
}
