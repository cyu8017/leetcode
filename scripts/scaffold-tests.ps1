param(
    [switch]$SkipIfExists
)

$ErrorActionPreference = "Stop"

. "$PSScriptRoot\lib\test-scaffold.ps1"

$repoRoot = Split-Path -Parent $PSScriptRoot
$folders = Get-ChildItem -Path $repoRoot -Directory | Where-Object { $_.Name -match '^\d{4}_' } | Sort-Object Name

$created = 0
$skipped = 0
$total = $folders.Count

foreach ($folder in $folders) {
    $number = [int]$folder.Name.Substring(0, 4)
    $params = @{
        RepoRoot = $repoRoot
        FolderName = $folder.Name
        Number = $number
    }
    if ($SkipIfExists) {
        $params.SkipIfExists = $true
    }

    $result = Add-ProblemTests @params
    if ($result.Status -eq "created") {
        $created++
    } else {
        $skipped++
    }

    $processed = $created + $skipped
    if ($processed % 250 -eq 0 -or $processed -eq $total) {
        Write-Host ("Progress: {0}/{1} (created: {2}, skipped: {3})" -f $processed, $total, $created, $skipped)
    }
}

Write-Host ""
Write-Host "Done."
Write-Host "Created: $created"
Write-Host "Skipped: $skipped"
Write-Host "Total: $total"
