# Test harness for 3709_design_exam_scores_tracker

Run tests with **Docker only** — no local Python, Java, Node, or compilers required. Toolchain versions are pinned in `docker/docker-compose.yml`.

## One-time setup (repository root)

```powershell
docker compose -f docker/docker-compose.yml build
```

```bash
docker compose -f docker/docker-compose.yml build
```

```zsh
docker compose -f docker/docker-compose.yml build
```

## Run by language (Docker)

### Windows (`scripts/test.ps1`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language python
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language javascript
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language typescript
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language java
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language cpp
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language c
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language go
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language rust
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language kotlin
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language swift
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language ruby
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language csharp
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language scala
./scripts/test.sh --folder 3709_design_exam_scores_tracker --language php
./scripts/test.sh --folder 3709_design_exam_scores_tracker --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3709_design_exam_scores_tracker --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm java java 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm c c 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm go go 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm rust rust 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm swift swift 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm scala scala 3709_design_exam_scores_tracker
docker compose -f docker/docker-compose.yml run --rm php php 3709_design_exam_scores_tracker
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3709_design_exam_scores_tracker` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3709_design_exam_scores_tracker` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3709_design_exam_scores_tracker` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3709_design_exam_scores_tracker` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3709_design_exam_scores_tracker` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3709_design_exam_scores_tracker` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3709_design_exam_scores_tracker` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3709_design_exam_scores_tracker` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3709_design_exam_scores_tracker` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3709_design_exam_scores_tracker` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3709_design_exam_scores_tracker` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3709_design_exam_scores_tracker` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3709_design_exam_scores_tracker` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3709_design_exam_scores_tracker` |

## Run from this folder (shortcuts)

Each `run_<language>.ps1` script in this directory calls Docker for you:

```powershell
.\run_python.ps1
.\run_javascript.ps1
.\run_java.ps1
.\run_cpp.ps1
# ... run_<language>.ps1 for all 14 languages
```

Run every language:

```powershell
.\run_all.ps1
```

Or from the repository root:

```powershell
.\scripts\test.ps1 -Folder 3709_design_exam_scores_tracker -AllLanguages
```

```bash
./scripts/test.sh --folder 3709_design_exam_scores_tracker --all-languages
```

```zsh
./scripts/test.sh --folder 3709_design_exam_scores_tracker --all-languages
```

## Files

| File | Purpose |
|------|---------|
| `config.json` | Solution class and method name |
| `cases.json` | Input/output test cases |
| `run_<language>.ps1` | Docker test launcher for one language |

## Add test cases

Edit `cases.json`:

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

Update `config.json` with the correct LeetCode method name:

```json
{
  "class": "Solution",
  "method": "twoSum",
  "paramOrder": ["nums", "target"]
}
```

For linked lists and trees, use array notation and set types in `config.json`:

```json
{
  "class": "Solution",
  "method": "addTwoNumbers",
  "types": {
    "l1": "listnode",
    "l2": "listnode",
    "return": "listnode"
  }
}
```
