param(
    [string]$Folder = "",
    [switch]$WarningsAsErrors,
    [int]$Limit = 0
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "validate-repo.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($Folder) { $args += @("--folder", $Folder) }
if ($WarningsAsErrors) { $args += "--warnings-as-errors" }
if ($Limit -gt 0) { $args += @("--limit", $Limit) }

python @args
exit $LASTEXITCODE
