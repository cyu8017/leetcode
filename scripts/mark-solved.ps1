param(
    [Parameter(Mandatory = $true)]
    [string]$Folder,

    [Parameter(Mandatory = $true)]
    [string]$Language,

    [switch]$Local,
    [switch]$SkipTest
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "mark-solved.py"
$args = @($pythonScript, "--repo-root", $repoRoot, "--folder", $Folder, "--language", $Language)

if ($Local) { $args += "--local" }
if ($SkipTest) { $args += "--skip-test" }

python @args
exit $LASTEXITCODE
