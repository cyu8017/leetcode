$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonScript = Join-Path $PSScriptRoot "sync-leetcode-status.py"
python $pythonScript --repo-root $repoRoot
exit $LASTEXITCODE
