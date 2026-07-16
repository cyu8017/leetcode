param(
    [Parameter(Mandatory = $true)]
    [string]$Folder,

    [string]$Language = "",
    [switch]$AllLanguages
)

$ErrorActionPreference = "Stop"

. "$PSScriptRoot\lib\test-scaffold.ps1"

$repoRoot = Split-Path -Parent $PSScriptRoot
$problemDir = Join-Path $repoRoot $Folder

if (-not (Test-Path $problemDir)) {
    Write-Error "Problem folder not found: $Folder"
}

if (-not (Test-Path (Join-Path $problemDir "tests\cases.json"))) {
    Write-Error "Missing tests folder. Run .\scripts\scaffold-tests.ps1 first."
}

function Invoke-LanguageTest {
    param(
        [string]$LangId
    )

    $definition = Get-TestLanguageDefinitions | Where-Object { $_.id -eq $LangId } | Select-Object -First 1
    if (-not $definition) {
        Write-Error "Unknown language: $LangId"
    }

    $command = $definition.runner
    $args = $definition.args | ForEach-Object {
        $_.Replace("{repo}", $repoRoot).Replace("{problemDir}", $problemDir)
    }

    Write-Host ""
    Write-Host "==> Testing $LangId"
    & $command @args
    return $LASTEXITCODE
}

if ($AllLanguages) {
    $failures = 0
    foreach ($definition in Get-TestLanguageDefinitions) {
        $exitCode = Invoke-LanguageTest -LangId $definition.id
        if ($exitCode -ne 0) {
            $failures++
        }
    }
    Write-Host ""
    Write-Host "All-language summary: $($failures) language runner(s) failed"
    exit $failures
}

if (-not $Language) {
    Write-Error "Specify -Language or -AllLanguages"
}

$exitCode = Invoke-LanguageTest -LangId $Language.ToLower()
exit $exitCode
