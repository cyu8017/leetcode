param(
    [switch]$UseCache,
    [switch]$Quiet,
    [switch]$JsonOutput,
    [string]$SourceUrl = ""
)

$ErrorActionPreference = "Stop"

. "$PSScriptRoot\lib\scaffold-problem.ps1"

$repoRoot = Split-Path -Parent $PSScriptRoot
$configPath = Join-Path $repoRoot "config\languages.json"
$sourcesPath = Join-Path $repoRoot "config\sources.json"
$languages = Get-Content $configPath | ConvertFrom-Json

if (-not $SourceUrl) {
    $sources = Get-Content $sourcesPath | ConvertFrom-Json
    $SourceUrl = $sources.leetcodeProblemsUrl
}

$params = @{
    RepoRoot = $repoRoot
    Languages = $languages
    SourceUrl = $SourceUrl
}
if ($UseCache) { $params.UseCache = $true }
if ($Quiet) { $params.Quiet = $true }

$report = Sync-LeetCodeProblems @params

if ($JsonOutput) {
    $report | ConvertTo-Json -Depth 5
    exit 0
}

if (-not $Quiet) {
    Write-Host ""
    if ($report.created -eq 0) {
        Write-Host "No new LeetCode problems found. Local repo is up to date ($($report.localFolderCount) folders)."
    } else {
        Write-Host "Created $($report.created) new problem folder(s):"
        foreach ($problem in $report.newProblems) {
            Write-Host "  - $($problem.FolderName) ($($problem.Difficulty))"
        }
    }
    Write-Host ""
    Write-Host "Sync report saved to config\last-sync.json"
}

exit 0
