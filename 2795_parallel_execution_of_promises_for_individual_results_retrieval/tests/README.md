# Test harness for 2795_parallel_execution_of_promises_for_individual_results_retrieval

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language python
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language javascript
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language typescript
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language java
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language cpp
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language c
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language go
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language rust
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language kotlin
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language swift
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language ruby
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language csharp
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language scala
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language php
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm java java 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm c c 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm go go 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm rust rust 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm swift swift 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm scala scala 2795_parallel_execution_of_promises_for_individual_results_retrieval
docker compose -f docker/docker-compose.yml run --rm php php 2795_parallel_execution_of_promises_for_individual_results_retrieval
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2795_parallel_execution_of_promises_for_individual_results_retrieval` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2795_parallel_execution_of_promises_for_individual_results_retrieval` |

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
.\scripts\test.ps1 -Folder 2795_parallel_execution_of_promises_for_individual_results_retrieval -AllLanguages
```

```bash
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --all-languages
```

```zsh
./scripts/test.sh --folder 2795_parallel_execution_of_promises_for_individual_results_retrieval --all-languages
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
