param(
    [switch]$ForceRefresh,
    [string]$SourceUrl = "https://raw.githubusercontent.com/bunnyxt/lcid/main/problems_all.json"
)

$ErrorActionPreference = "Stop"

$params = @{
    SourceUrl = $SourceUrl
}
if (-not $ForceRefresh) {
    $params.UseCache = $true
}

& "$PSScriptRoot\sync-new-problems.ps1" @params
