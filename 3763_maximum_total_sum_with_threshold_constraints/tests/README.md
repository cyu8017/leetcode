# Test harness for 3763_maximum_total_sum_with_threshold_constraints

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language python
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language javascript
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language typescript
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language java
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language cpp
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language c
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language go
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language rust
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language kotlin
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language swift
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language ruby
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language csharp
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language scala
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language php
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm java java 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm c c 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm go go 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm rust rust 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm swift swift 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm scala scala 3763_maximum_total_sum_with_threshold_constraints
docker compose -f docker/docker-compose.yml run --rm php php 3763_maximum_total_sum_with_threshold_constraints
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3763_maximum_total_sum_with_threshold_constraints` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3763_maximum_total_sum_with_threshold_constraints` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3763_maximum_total_sum_with_threshold_constraints` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3763_maximum_total_sum_with_threshold_constraints` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3763_maximum_total_sum_with_threshold_constraints` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3763_maximum_total_sum_with_threshold_constraints` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3763_maximum_total_sum_with_threshold_constraints` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3763_maximum_total_sum_with_threshold_constraints` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3763_maximum_total_sum_with_threshold_constraints` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3763_maximum_total_sum_with_threshold_constraints` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3763_maximum_total_sum_with_threshold_constraints` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3763_maximum_total_sum_with_threshold_constraints` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3763_maximum_total_sum_with_threshold_constraints` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3763_maximum_total_sum_with_threshold_constraints` |

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
.\scripts\test.ps1 -Folder 3763_maximum_total_sum_with_threshold_constraints -AllLanguages
```

```bash
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --all-languages
```

```zsh
./scripts/test.sh --folder 3763_maximum_total_sum_with_threshold_constraints --all-languages
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
