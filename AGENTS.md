# LeetCode Solutions — Agent Instructions

This repository uses an automated sync workflow to keep problem folders aligned with LeetCode.

## Primary task: sync new LeetCode problems

When the user asks to sync, check for new problems, update folders, or maintain the problem tree, run:

```powershell
.\scripts\sync-new-problems.ps1
```

This script:

1. Fetches the latest LeetCode problem list from the configured source
2. Compares it against existing `{number}_{title}` folders in the repo root
3. Creates folders with solution stubs in all 14 languages for any new problems
4. Updates `config/problems.json` and writes a report to `config/last-sync.json`

### When to run sync automatically

Run sync at the start of a session when:

- The user asks about new LeetCode questions
- The user wants the repo updated from LeetCode
- You are about to add solutions and the problem folder may not exist yet

Do **not** re-scaffold folders that already exist. The sync script skips them.

## Testing solutions

**Use Docker** so everyone runs the same pinned toolchains (Python 3.12, Node 20, JDK 21, GCC 14, etc.) regardless of host OS.

```powershell
docker compose -f docker/docker-compose.yml build
.\scripts\test.ps1 -Folder 0001_two_sum -Language python
.\scripts\test.ps1 -Folder 0087_scramble_string -Language cpp
```

macOS / Linux: `./scripts/test.sh --folder 0001_two_sum --language python`

Use `-Local` only when intentionally testing against host-installed runtimes.

### Run all solved problems

Problems with passing implementations are listed in `config/solved-problems.json`. Run them in batch:

```powershell
.\scripts\run-solved.ps1
.\scripts\run-solved.ps1 -Language python
.\scripts\run-solved.ps1 -Local
```

macOS / Linux: `./scripts/run-solved.sh`

When a solution passes tests, add an entry to `config/solved-problems.json` so CI and `run-solved` pick it up.

## LeetCode account sync (import / submit)

Requires browser cookies in `.leetcode.env` (copy from `.leetcode.env.example`):

```powershell
Copy-Item .leetcode.env.example .leetcode.env
# Edit .leetcode.env with LEETCODE_SESSION and LEETCODE_CSRF from DevTools
```

**Import** your accepted submissions into local solution files:

```powershell
.\scripts\import-from-leetcode.ps1 -Folder 0001_two_sum
.\scripts\import-from-leetcode.ps1 -Number 1 -Language python
.\scripts\import-from-leetcode.ps1 -All -DryRun
.\scripts\import-from-leetcode.ps1 -All -Overwrite -Limit 50
.\scripts\import-from-leetcode.ps1 -All -AllLanguages -Overwrite
```

**Submit** or **run** a local solution on LeetCode:

```powershell
.\scripts\submit-to-leetcode.ps1 -Folder 0001_two_sum -Language python
.\scripts\submit-to-leetcode.ps1 -Number 1 -Language python -TestLocal
.\scripts\submit-to-leetcode.ps1 -Folder 0001_two_sum -Language python -RunOnly
```

**Sync solved status** from your account to `config/leetcode-solved.json`:

```powershell
.\scripts\sync-leetcode-status.ps1
```

Never commit `.leetcode.env` or session cookies.

## Validation and quality gates

Validate all problem folders and test JSON:

```powershell
.\scripts\validate-repo.ps1
.\scripts\validate-repo.ps1 -Folder 0001_two_sum
python -m unittest discover -s scripts/tests -p "test_*.py"
```

Refresh `tests/config.json` method names from LeetCode metadata (without overwriting cases):

```powershell
.\scripts\sync-test-config.ps1 -Number 1 -Force
.\scripts\sync-test-config.ps1 -Force -DryRun
```

Re-sync legacy database test cases from README (structured `kind: sql`):

```powershell
.\scripts\resync-database-cases.ps1
.\scripts\resync-database-cases.ps1 -DryRun
```

Run smoke tests (representative problems in `config/smoke-problems.json`):

```powershell
.\scripts\run-smoke.ps1
```

Mark a problem as solved after tests pass:

```powershell
.\scripts\mark-solved.ps1 -Folder 0001_two_sum -Language python -Local
```

Optional pre-commit hooks:

```powershell
pip install pre-commit
pre-commit install
```

### CI

GitHub Actions workflow `.github/workflows/test-solutions.yml` runs validation, smoke tests, and `python scripts/run-solved.py` (Docker) on push and pull requests to `main`/`master`.

Each problem folder contains `tests/cases.json`, `tests/config.json`, and `tests/run_<language>.ps1` for all 14 languages.

To populate example test cases from public LeetCode datasets (neenza JSON + README/HTML fallbacks):

```powershell
.\scripts\sync-test-cases.ps1
```

Use `-Force` to overwrite existing cases, `-Number 54` for one problem, or `-DryRun` to preview.

Design problems (`kind: "design"` in `tests/cases.json`) run operation sequences (constructor + method calls). Use the design class name in your solution file (e.g. `WordDistance`, not `Solution`). Sync design configs with:

```powershell
python scripts/sync-design-configs.py
```

When new problems are synced, their README is populated automatically. To refresh all problem statements:

```powershell
.\scripts\update-problem-readmes.ps1
```

### Reading sync results

After sync, read `config/last-sync.json`:

- `created` — number of new folders added this run
- `newProblems` — list of newly scaffolded problems
- `remoteCount` vs `localFolderCount` — sanity check totals

If `created` is 0, tell the user the repo is already up to date.

## Folder conventions

- Format: `{4-digit-number}_{snake_case_title}` (example: `0001_two_sum`)
- Each folder contains `README.md` plus solution files for Python, Java, JavaScript, TypeScript, C++, C, Go, Rust, Kotlin, Swift, Ruby, C#, Scala, PHP

## Manual scaffolding

To add a single problem by hand:

```powershell
.\scripts\new-problem.ps1 -Number 42 -Title "trapping_rain_water" -Difficulty Medium -Tags "array,two-pointers"
```

## Hooks

A Cursor `sessionStart` hook runs sync automatically when you open this project. Check `config/last-sync.json` if new folders were created before your first response.
