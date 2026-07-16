# Test harness for 1203_sort_items_by_groups_respecting_dependencies

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language python
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language javascript
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language typescript
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language java
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language cpp
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language c
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language go
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language rust
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language kotlin
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language swift
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language ruby
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language csharp
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language scala
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language php
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm java java 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm c c 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm go go 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm rust rust 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm swift swift 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm scala scala 1203_sort_items_by_groups_respecting_dependencies
docker compose -f docker/docker-compose.yml run --rm php php 1203_sort_items_by_groups_respecting_dependencies
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1203_sort_items_by_groups_respecting_dependencies` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1203_sort_items_by_groups_respecting_dependencies` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1203_sort_items_by_groups_respecting_dependencies` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1203_sort_items_by_groups_respecting_dependencies` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1203_sort_items_by_groups_respecting_dependencies` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1203_sort_items_by_groups_respecting_dependencies` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1203_sort_items_by_groups_respecting_dependencies` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1203_sort_items_by_groups_respecting_dependencies` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1203_sort_items_by_groups_respecting_dependencies` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1203_sort_items_by_groups_respecting_dependencies` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1203_sort_items_by_groups_respecting_dependencies` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1203_sort_items_by_groups_respecting_dependencies` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1203_sort_items_by_groups_respecting_dependencies` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1203_sort_items_by_groups_respecting_dependencies` |

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
.\scripts\test.ps1 -Folder 1203_sort_items_by_groups_respecting_dependencies -AllLanguages
```

```bash
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --all-languages
```

```zsh
./scripts/test.sh --folder 1203_sort_items_by_groups_respecting_dependencies --all-languages
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
