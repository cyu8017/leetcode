param(
    [Parameter(Mandatory = $true)]
    [int]$Number,

    [Parameter(Mandatory = $true)]
    [string]$Title,

    [string]$TitleSlug = "",
    [string]$Difficulty = "Easy",
    [string]$Tags = "",
    [switch]$SkipIfExists
)

$ErrorActionPreference = "Stop"

. "$PSScriptRoot\lib\scaffold-problem.ps1"

$repoRoot = Split-Path -Parent $PSScriptRoot
$configPath = Join-Path $repoRoot "config\languages.json"
$languages = Get-Content $configPath | ConvertFrom-Json

if (-not $TitleSlug) {
    $TitleSlug = $Title.ToLower() -replace '[\s_]+', '-'
}

$displayTitle = ($Title -replace '_', ' ')
$params = @{
    RepoRoot = $repoRoot
    Languages = $languages
    Number = $Number
    TitleSlug = $TitleSlug
    DisplayTitle = $displayTitle
    Difficulty = $Difficulty
    Tags = $Tags
}
if ($SkipIfExists) {
    $params.SkipIfExists = $true
}

$result = New-ProblemScaffold @params

Write-Host "$($result.Status): $($result.FolderName)"
Write-Host "Path: $(Join-Path $repoRoot $result.FolderName)"
