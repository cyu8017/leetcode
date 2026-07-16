$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$syncScript = Join-Path $repoRoot "scripts\sync-new-problems.ps1"

try {
    $reportJson = & $syncScript -Quiet -JsonOutput 2>$null
    if (-not $reportJson) {
        Write-Output '{"continue": true}'
        exit 0
    }

    $report = $reportJson | ConvertFrom-Json

    if ($report.created -gt 0) {
        $names = ($report.newProblems | ForEach-Object { $_.FolderName }) -join ", "
        $context = @"
LeetCode sync completed on session start.
Created $($report.created) new problem folder(s): $names
Read config/last-sync.json for details. Existing folders were not modified.
"@
        $payload = @{
            continue = $true
            additional_context = $context
        }
        $payload | ConvertTo-Json -Compress
    } else {
        Write-Output '{"continue": true}'
    }
} catch {
    $payload = @{
        continue = $true
        additional_context = "LeetCode sync hook failed: $($_.Exception.Message). Run .\scripts\sync-new-problems.ps1 manually."
    }
    $payload | ConvertTo-Json -Compress
}

exit 0
