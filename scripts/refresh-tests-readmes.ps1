param(
    [switch]$SkipIfMissing
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$templatePath = Join-Path $repoRoot "config\tests-readme.template.md"
$template = Get-Content $templatePath -Raw -Encoding UTF8

. "$PSScriptRoot\lib\test-scaffold.ps1"

$folders = Get-ChildItem -Path $repoRoot -Directory | Where-Object { $_.Name -match '^\d{4}_' } | Sort-Object Name
$updated = 0
$skipped = 0

foreach ($folder in $folders) {
    $testsDir = Join-Path $folder.FullName "tests"
    if (-not (Test-Path $testsDir)) {
        if ($SkipIfMissing) {
            $skipped++
            continue
        }
        $number = [int]$folder.Name.Substring(0, 4)
        Add-ProblemTests -RepoRoot $repoRoot -FolderName $folder.Name -Number $number | Out-Null
        $updated++
        continue
    }

    $content = $template.Replace("{PROBLEM_NAME}", $folder.Name)
    Set-Utf8NoBomContent -Path (Join-Path $testsDir "README.md") -Value $content
    $updated++

    if ($updated % 250 -eq 0) {
        Write-Host "Updated $updated tests/README.md files..."
    }
}

Write-Host "Done. Updated: $updated, skipped: $skipped"
