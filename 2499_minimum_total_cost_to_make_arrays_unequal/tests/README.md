# Test harness for 2499_minimum_total_cost_to_make_arrays_unequal

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language python
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language javascript
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language typescript
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language java
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language cpp
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language c
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language go
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language rust
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language kotlin
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language swift
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language ruby
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language csharp
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language scala
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language php
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm java java 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm c c 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm go go 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm rust rust 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm swift swift 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm scala scala 2499_minimum_total_cost_to_make_arrays_unequal
docker compose -f docker/docker-compose.yml run --rm php php 2499_minimum_total_cost_to_make_arrays_unequal
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2499_minimum_total_cost_to_make_arrays_unequal` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2499_minimum_total_cost_to_make_arrays_unequal` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2499_minimum_total_cost_to_make_arrays_unequal` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2499_minimum_total_cost_to_make_arrays_unequal` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2499_minimum_total_cost_to_make_arrays_unequal` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2499_minimum_total_cost_to_make_arrays_unequal` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2499_minimum_total_cost_to_make_arrays_unequal` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2499_minimum_total_cost_to_make_arrays_unequal` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2499_minimum_total_cost_to_make_arrays_unequal` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2499_minimum_total_cost_to_make_arrays_unequal` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2499_minimum_total_cost_to_make_arrays_unequal` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2499_minimum_total_cost_to_make_arrays_unequal` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2499_minimum_total_cost_to_make_arrays_unequal` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2499_minimum_total_cost_to_make_arrays_unequal` |

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
.\scripts\test.ps1 -Folder 2499_minimum_total_cost_to_make_arrays_unequal -AllLanguages
```

```bash
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --all-languages
```

```zsh
./scripts/test.sh --folder 2499_minimum_total_cost_to_make_arrays_unequal --all-languages
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
