param(
    [switch]$ForceRefresh,
    [switch]$FetchPremium,
    [int]$Number = 0,
    [string]$LeetcodeSession = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "update-problem-readmes.py"
$args = @($pythonScript, "--repo-root", $repoRoot)

if ($ForceRefresh) {
    $args += "--force-refresh"
}
if ($FetchPremium) {
    $args += "--fetch-premium"
}
if ($LeetcodeSession) {
    $args += @("--leetcode-session", $LeetcodeSession)
}
if ($Number -gt 0) {
    $args += @("--number", $Number)
}

python @args
