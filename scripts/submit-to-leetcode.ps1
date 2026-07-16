param(
    [Parameter(Mandatory = $true)]
    [string]$Language,

    [string]$Folder = "",
    [int]$Number = 0,
    [switch]$RunOnly,
    [switch]$TestLocal,
    [double]$Timeout = 120
)

$ErrorActionPreference = "Stop"

if (-not $Folder -and $Number -le 0) {
    Write-Error "Provide -Folder or -Number"
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "submit-to-leetcode.py"
$args = @($pythonScript, "--repo-root", $repoRoot, "--language", $Language, "--timeout", $Timeout)

if ($Folder) { $args += @("--folder", $Folder) }
if ($Number -gt 0) { $args += @("--number", $Number) }
if ($RunOnly) { $args += "--run-only" }
if ($TestLocal) { $args += "--test-local" }

python @args
exit $LASTEXITCODE
