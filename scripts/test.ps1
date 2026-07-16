param(
    [Parameter(Mandatory = $true)]
    [string]$Folder,

    [string]$Language = "",
    [switch]$AllLanguages,
    [switch]$Local
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $repoRoot "docker\docker-compose.yml"

function Test-DockerAvailable {
    return [bool](Get-Command docker -ErrorAction SilentlyContinue)
}

function Invoke-DockerLanguageTest {
    param([string]$LangId)

    Write-Host ""
    Write-Host "==> Testing $LangId (Docker)"
    docker compose -f $composeFile run --rm $LangId $LangId $Folder
    return $LASTEXITCODE
}

if (-not $Local) {
    if (-not (Test-DockerAvailable)) {
        Write-Error "Docker is required. Install Docker Desktop, or pass -Local to use host toolchains."
    }

    if ($AllLanguages) {
        $languages = @(
            "python", "javascript", "typescript", "java", "ruby", "php",
            "cpp", "c", "go", "rust", "csharp", "kotlin", "scala", "swift"
        )
        $failures = 0
        foreach ($lang in $languages) {
            $exitCode = Invoke-DockerLanguageTest -LangId $lang
            if ($exitCode -ne 0) { $failures++ }
        }
        Write-Host ""
        Write-Host "All-language summary: $failures language runner(s) failed"
        exit $failures
    }

    if (-not $Language) {
        Write-Error "Specify -Language or -AllLanguages"
    }

    $exitCode = Invoke-DockerLanguageTest -LangId $Language.ToLower()
    exit $exitCode
}

$params = @{
    Folder = $Folder
}
if ($Language) { $params.Language = $Language }
if ($AllLanguages) { $params.AllLanguages = $true }

& (Join-Path $PSScriptRoot "test-problem.ps1") @params
