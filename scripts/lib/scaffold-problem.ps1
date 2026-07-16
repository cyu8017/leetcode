function ConvertTo-SnakeCaseTitle {
    param([string]$TitleSlug)
    return $TitleSlug.ToLower() -replace '-', '_'
}

function Get-ProblemFolderName {
    param(
        [int]$Number,
        [string]$TitleSlug
    )
    $paddedNumber = "{0:D4}" -f $Number
    $normalizedTitle = ConvertTo-SnakeCaseTitle -TitleSlug $TitleSlug
    return "${paddedNumber}_${normalizedTitle}"
}

function Get-LanguageStub {
    param(
        [object]$Language,
        [string]$PaddedNumber,
        [string]$DisplayTitle,
        [string]$TitleSlug
    )

    $header = "$($Language.comment) LeetCode $PaddedNumber - $DisplayTitle`n$($Language.comment) https://leetcode.com/problems/$TitleSlug/`n`n"

    switch ($Language.id) {
        "python" {
            return $header + @"
class Solution:
    def solve(self) -> None:
        pass
"@
        }
        "java" {
            return $header + @"
class Solution {
    public void solve() {
    }
}
"@
        }
        "javascript" {
            return $header + @"
/**
 * @param {any} input
 * @return {any}
 */
var solve = function(input) {
};
"@
        }
        "typescript" {
            return $header + @"
function solve(input: unknown): unknown {
    return null;
}
"@
        }
        "cpp" {
            return $header + @"
class Solution {
public:
    void solve() {
    }
};
"@
        }
        "c" {
            return $header + @"
void solve() {
}
"@
        }
        "go" {
            return $header + @"
func solve() {
}
"@
        }
        "rust" {
            return $header + @"
impl Solution {
    pub fn solve() {
    }
}
"@
        }
        "kotlin" {
            return $header + @"
class Solution {
    fun solve() {
    }
}
"@
        }
        "swift" {
            return $header + @"
class Solution {
    func solve() {
    }
}
"@
        }
        "ruby" {
            return $header + @"
# @param {Object} input
# @return {Object}
def solve(input)
end
"@
        }
        "csharp" {
            return $header + @"
public class Solution {
    public void Solve() {
    }
}
"@
        }
        "scala" {
            return $header + @"
object Solution {
  def solve(): Unit = {}
}
"@
        }
        "php" {
            return $header + @"
class Solution {
    function solve() {
    }
}
"@
        }
        default {
            throw "Unsupported language id: $($Language.id)"
        }
    }
}

function New-ProblemScaffold {
    param(
        [string]$RepoRoot,
        [object[]]$Languages,
        [int]$Number,
        [string]$TitleSlug,
        [string]$DisplayTitle,
        [string]$Difficulty = "Easy",
        [string]$Tags = "",
        [switch]$SkipIfExists
    )

    $paddedNumber = "{0:D4}" -f $Number
    $folderName = Get-ProblemFolderName -Number $Number -TitleSlug $TitleSlug
    $problemDir = Join-Path $RepoRoot $folderName

    if (Test-Path $problemDir) {
        if ($SkipIfExists) {
            return [pscustomobject]@{
                Status = "skipped"
                FolderName = $folderName
            }
        }
        throw "Problem folder already exists: $folderName"
    }

    New-Item -ItemType Directory -Path $problemDir | Out-Null

    $leetcodeUrl = "https://leetcode.com/problems/$TitleSlug/"
    $tagLine = if ($Tags) { "**Tags:** $Tags`n" } else { "" }

    $readme = @"
# $paddedNumber. $DisplayTitle

- **Difficulty:** $Difficulty
- **LeetCode:** [$leetcodeUrl]($leetcodeUrl)
${tagLine}
## Approach

<!-- Describe your solution approach here -->

"@

    Set-Content -Path (Join-Path $problemDir "README.md") -Value $readme -Encoding UTF8 -NoNewline

    foreach ($lang in $Languages) {
        $stub = Get-LanguageStub -Language $lang -PaddedNumber $paddedNumber -DisplayTitle $DisplayTitle -TitleSlug $TitleSlug
        Set-Content -Path (Join-Path $problemDir $lang.file) -Value $stub -Encoding UTF8 -NoNewline
    }

    . (Join-Path $PSScriptRoot "test-scaffold.ps1")
    Add-ProblemTests -RepoRoot $RepoRoot -FolderName $folderName -Number $Number | Out-Null

    $updateScript = Join-Path (Split-Path -Parent $PSScriptRoot) "update-problem-readmes.py"
    if (Test-Path $updateScript) {
        python $updateScript --repo-root $RepoRoot --number $Number 2>$null | Out-Null
    }

    return [pscustomobject]@{
        Status = "created"
        FolderName = $folderName
    }
}

function Get-LeetCodeProblems {
    param(
        [string]$SourceUrl = "https://raw.githubusercontent.com/bunnyxt/lcid/main/problems_all.json"
    )

    $raw = Invoke-RestMethod -Uri $SourceUrl -TimeoutSec 120
    $problems = @()

    foreach ($property in $raw.PSObject.Properties) {
        $entry = $property.Value
        $tags = if ($entry.topicTags) {
            ($entry.topicTags | ForEach-Object { $_.slug }) -join ","
        } else {
            ""
        }

        $problems += [pscustomobject]@{
            Number = [int]$entry.frontendQuestionId
            TitleSlug = $entry.titleSlug
            DisplayTitle = $entry.title
            Difficulty = $entry.difficulty
            Tags = $tags
        }
    }

    return $problems | Sort-Object Number
}

function Sync-LeetCodeProblems {
    param(
        [string]$RepoRoot,
        [object[]]$Languages,
        [string]$SourceUrl = "https://raw.githubusercontent.com/bunnyxt/lcid/main/problems_all.json",
        [switch]$UseCache,
        [switch]$Quiet
    )

    $problemsCachePath = Join-Path $RepoRoot "config\problems.json"
    $lastSyncPath = Join-Path $RepoRoot "config\last-sync.json"

    if ($UseCache -and (Test-Path $problemsCachePath)) {
        $remoteProblems = Get-Content $problemsCachePath | ConvertFrom-Json
        if (-not $Quiet) {
            Write-Host "Using cached problem list ($($remoteProblems.Count) problems)."
        }
    } else {
        if (-not $Quiet) {
            Write-Host "Scanning LeetCode for problems..."
        }
        $remoteProblems = Get-LeetCodeProblems -SourceUrl $SourceUrl
        $remoteProblems | ConvertTo-Json -Depth 4 | Set-Content -Path $problemsCachePath -Encoding UTF8
        if (-not $Quiet) {
            Write-Host "Fetched $($remoteProblems.Count) problems from LeetCode."
        }
    }

    $created = 0
    $skipped = 0
    $newProblems = @()

    foreach ($problem in $remoteProblems) {
        $result = New-ProblemScaffold `
            -RepoRoot $RepoRoot `
            -Languages $Languages `
            -Number $problem.Number `
            -TitleSlug $problem.TitleSlug `
            -DisplayTitle $problem.DisplayTitle `
            -Difficulty $problem.Difficulty `
            -Tags $problem.Tags `
            -SkipIfExists

        if ($result.Status -eq "created") {
            $created++
            $newProblems += [pscustomobject]@{
                Number = $problem.Number
                Title = $problem.DisplayTitle
                TitleSlug = $problem.TitleSlug
                Difficulty = $problem.Difficulty
                FolderName = $result.FolderName
            }
            if (-not $Quiet) {
                Write-Host "Created $($result.FolderName)"
            }
        } else {
            $skipped++
        }
    }

    $localFolders = @(Get-ChildItem -Path $RepoRoot -Directory | Where-Object { $_.Name -match '^\d{4}_' })
    $report = [pscustomobject]@{
        syncedAt = (Get-Date).ToUniversalTime().ToString("o")
        sourceUrl = $SourceUrl
        remoteCount = $remoteProblems.Count
        localFolderCount = $localFolders.Count
        created = $created
        skipped = $skipped
        newProblems = $newProblems
    }

    $report | ConvertTo-Json -Depth 5 | Set-Content -Path $lastSyncPath -Encoding UTF8

    return $report
}
