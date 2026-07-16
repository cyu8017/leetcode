# LeetCode Solutions

Organized solutions for LeetCode problems, with one folder per question and implementations in every supported language.

## Folder Structure

Each problem lives in its own directory at the repository root:

```
{question_number}_{question_title}/
├── README.md          # Problem link, difficulty, tags, notes
├── solution.py        # Python 3
├── Solution.java      # Java
├── solution.js        # JavaScript
├── solution.ts        # TypeScript
├── solution.cpp       # C++
├── solution.c         # C
├── solution.go        # Go
├── solution.rs        # Rust
├── Solution.kt        # Kotlin
├── Solution.swift     # Swift
├── solution.rb        # Ruby
├── Solution.cs        # C#
├── Solution.scala     # Scala
└── solution.php       # PHP
```

### Naming Convention

| Part | Rule | Example |
|------|------|---------|
| Question number | Zero-padded to 4 digits | `0001`, `0142`, `2000` |
| Question title | Lowercase, words separated by `_` | `two_sum`, `add_two_numbers` |
| Full folder name | `{number}_{title}` | `0001_two_sum` |

## Adding a New Problem

Use the scaffold script from the repository root:

```powershell
.\scripts\new-problem.ps1 -Number 3 -Title "longest_substring_without_repeating_characters"
```

Optional flags:

```powershell
.\scripts\new-problem.ps1 -Number 42 -Title "trapping_rain_water" -Difficulty Medium -Tags "array,two-pointers"
```

This creates the folder, all language solution stubs, and a problem `README.md`.

### Sync New Problems (recommended)

Scan LeetCode for newly published questions and scaffold only missing folders:

```powershell
.\scripts\sync-new-problems.ps1
```

This runs automatically when you open the project in Cursor (via a `sessionStart` hook). Results are saved to `config/last-sync.json`.

### Scaffold All Problems

To generate folders for every LeetCode problem (currently **3,985**):

```powershell
.\scripts\scaffold-all.ps1
```

This downloads the latest problem list, caches it in `config/problems.json`, and creates any missing folders. Existing folders are skipped.

To refresh the problem list from LeetCode:

```powershell
.\scripts\scaffold-all.ps1 -ForceRefresh
```

## Testing Solutions

**Docker is the recommended way to run tests.** Collaborators only need Docker — not local Python, Java, Node, or compilers. Toolchain versions are pinned in `docker/docker-compose.yml`.

### Prerequisites

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows, macOS, or Linux)
2. One-time image build:

```powershell
docker compose -f docker/docker-compose.yml build
```

### Run tests (Docker)

```powershell
# Windows
.\scripts\test.ps1 -Folder 0001_two_sum -Language python
.\scripts\test.ps1 -Folder 0087_scramble_string -Language cpp
.\scripts\test.ps1 -Folder 0001_two_sum -AllLanguages
```

```bash
# macOS / Linux
./scripts/test.sh --folder 0001_two_sum --language python
./scripts/test.sh --folder 0001_two_sum --all-languages
```

From inside a problem folder (also uses Docker):

```powershell
.\tests\run_python.ps1
.\tests\run_cpp.ps1
.\tests\run_all.ps1
```

See `docker/README.md` for pinned toolchain versions.

### Local fallback (optional)

If you pass `-Local`, tests use whatever is installed on your machine:

```powershell
.\scripts\test.ps1 -Folder 0001_two_sum -Language python -Local
```

Every problem folder includes a `tests/` directory with:

| File | Purpose |
|------|---------|
| `config.json` | Solution class and method name |
| `cases.json` | Input/output test cases |
| `run_<language>.ps1` | Run tests via Docker for one language (14 launchers) |
| `run_all.ps1` | Run all language test runners via Docker |

### Run tests for one problem (legacy local command)

```powershell
.\scripts\test-problem.ps1 -Folder 0001_two_sum -Language python
```

Prefer `.\scripts\test.ps1` instead — it runs inside Docker by default.

### Add test cases

Edit `tests/cases.json` inside the problem folder:

```json
{
  "cases": [
    {
      "args": { "nums": [2, 7, 11, 15], "target": 9 },
      "expected": [0, 1]
    }
  ]
}
```

Update `tests/config.json` with the LeetCode method name and optional `paramOrder`:

```json
{
  "class": "Solution",
  "method": "twoSum",
  "paramOrder": ["nums", "target"]
}
```

Sample cases for problems 1–3 live in `config/problem-test-overrides.json`. Add more overrides there, then rerun:

```powershell
.\scripts\scaffold-tests.ps1 -SkipIfExists
```

### Scaffold tests for all problems

```powershell
.\scripts\scaffold-tests.ps1
```

New problems created by sync automatically include a `tests/` folder.

### Problem descriptions in README files

Each problem `README.md` includes the full LeetCode statement under `## Problem`.

To refresh descriptions from LeetCode:

```powershell
.\scripts\update-problem-readmes.ps1
```

Update one problem:

```powershell
.\scripts\update-problem-readmes.ps1 -Number 173
```

Force re-download of cached question data:

```powershell
.\scripts\update-problem-readmes.ps1 -ForceRefresh
```

### Agent automation

- **`AGENTS.md`** — instructions for Cursor agents to run sync on request
- **`.cursor/hooks.json`** — auto-sync on project session start
- **`.cursor/skills/sync-leetcode/`** — skill for manual sync tasks

## Problem Index

All **3,985** problem folders are scaffolded at the repository root (`0001_two_sum` through `3985_palindromic_subarray_sum`).

See `config/problems.json` for the full searchable list with number, title, difficulty, and tags.

| # | Title | Difficulty |
|---|-------|------------|
| [0001](0001_two_sum) | Two Sum | Easy |
| [0002](0002_add_two_numbers) | Add Two Numbers | Medium |
| [3985](3985_palindromic_subarray_sum) | Palindromic Subarray Sum | Hard |

## Languages

All 14 LeetCode-supported languages are included for every problem:

Python 3, Java, JavaScript, TypeScript, C++, C, Go, Rust, Kotlin, Swift, Ruby, C#, Scala, PHP
