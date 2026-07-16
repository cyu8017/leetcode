function Set-Utf8NoBomContent {
    param(
        [string]$Path,
        [string]$Value
    )

    $encoding = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Value, $encoding)
}

function Get-TestLanguageDefinitions {
    return @(
        @{ id = "python";     runner = "python"; args = @("{repo}\runners\python\run_tests.py", "{problemDir}") },
        @{ id = "javascript"; runner = "node";   args = @("{repo}\runners\javascript\run_tests.mjs", "{problemDir}") },
        @{ id = "java";       runner = "python"; args = @("{repo}\runners\java\run_tests.py", "{problemDir}") },
        @{ id = "typescript"; runner = "node"; args = @("{repo}\runners\typescript\run_tests.mjs", "{problemDir}") },
        @{ id = "ruby";       runner = "ruby";  args = @("{repo}\runners\ruby\run_tests.rb", "{problemDir}") },
        @{ id = "php";        runner = "php";   args = @("{repo}\runners\php\run_tests.php", "{problemDir}") },
        @{ id = "cpp";        runner = "python"; args = @("{repo}\runners\cpp\run_tests.py", "{problemDir}") },
        @{ id = "c";          runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "c", "{problemDir}") },
        @{ id = "go";         runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "go", "{problemDir}") },
        @{ id = "rust";       runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "rust", "{problemDir}") },
        @{ id = "kotlin";     runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "kotlin", "{problemDir}") },
        @{ id = "csharp";     runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "csharp", "{problemDir}") },
        @{ id = "scala";      runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "scala", "{problemDir}") },
        @{ id = "swift";      runner = "python"; args = @("{repo}\runners\compiled\run_compiled.py", "swift", "{problemDir}") }
    )
}

function Get-ProblemTestConfig {
    param(
        [int]$Number,
        [string]$RepoRoot
    )

    $overridesPath = Join-Path $RepoRoot "config\problem-test-overrides.json"
    $defaultConfigPath = Join-Path $RepoRoot "config\test-config.default.json"
    $defaultCasesPath = Join-Path $RepoRoot "config\test-cases.default.json"

    $defaultConfig = Get-Content $defaultConfigPath -Raw | ConvertFrom-Json
    $defaultCases = Get-Content $defaultCasesPath -Raw | ConvertFrom-Json

    if (Test-Path $overridesPath) {
        $overrides = Get-Content $overridesPath -Raw | ConvertFrom-Json
        $key = [string]$Number
        if ($overrides.PSObject.Properties.Name -contains $key) {
            $override = $overrides.$key
            return [pscustomobject]@{
                Config = $override
                Cases = [pscustomobject]@{ cases = @($override.cases) }
            }
        }
    }

    return [pscustomobject]@{
        Config = $defaultConfig
        Cases = $defaultCases
    }
}

function Add-ProblemTests {
    param(
        [string]$RepoRoot,
        [string]$FolderName,
        [int]$Number,
        [switch]$SkipIfExists
    )

    $testsDir = Join-Path (Join-Path $RepoRoot $FolderName) "tests"
    if ((Test-Path $testsDir) -and $SkipIfExists) {
        return [pscustomobject]@{ Status = "skipped"; FolderName = $FolderName }
    }

    New-Item -ItemType Directory -Path $testsDir -Force | Out-Null

    $testData = Get-ProblemTestConfig -Number $Number -RepoRoot $RepoRoot
    $configObject = $testData.Config | Select-Object class, method, paramOrder, types, description
    $readmeTemplate = Get-Content (Join-Path $RepoRoot "config\tests-readme.template.md") -Raw -Encoding UTF8
    Set-Utf8NoBomContent -Path (Join-Path $testsDir "config.json") -Value ($configObject | ConvertTo-Json -Depth 6)
    Set-Utf8NoBomContent -Path (Join-Path $testsDir "cases.json") -Value ($testData.Cases | ConvertTo-Json -Depth 10)
    Set-Utf8NoBomContent -Path (Join-Path $testsDir "README.md") -Value ($readmeTemplate.Replace("{PROBLEM_NAME}", $FolderName))

    $languages = Get-TestLanguageDefinitions
    foreach ($lang in $languages) {
        $launcher = @"
`$ErrorActionPreference = "Stop"
`$repoRoot = Split-Path -Parent (Split-Path -Parent `$PSScriptRoot)
& "$repoRoot\scripts\test.ps1" -Folder "$FolderName" -Language "$($lang.id)"
"@
        Set-Content -Path (Join-Path $testsDir "run_$($lang.id).ps1") -Value $launcher -Encoding UTF8
    }

    $runAll = @"
`$ErrorActionPreference = "Continue"
`$repoRoot = Split-Path -Parent (Split-Path -Parent `$PSScriptRoot)
& "$repoRoot\scripts\test.ps1" -Folder "$FolderName" -AllLanguages
"@
    Set-Content -Path (Join-Path $testsDir "run_all.ps1") -Value $runAll -Encoding UTF8

    return [pscustomobject]@{
        Status = "created"
        FolderName = $FolderName
    }
}
