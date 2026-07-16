# Test harness for 2167_minimum_time_to_remove_all_cars_containing_illegal_goods

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language python
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language javascript
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language typescript
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language java
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language cpp
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language c
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language go
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language rust
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language kotlin
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language swift
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language ruby
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language csharp
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language scala
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language php
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm java java 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm c c 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm go go 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm rust rust 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm swift swift 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm scala scala 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
docker compose -f docker/docker-compose.yml run --rm php php 2167_minimum_time_to_remove_all_cars_containing_illegal_goods
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2167_minimum_time_to_remove_all_cars_containing_illegal_goods` |

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
.\scripts\test.ps1 -Folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods -AllLanguages
```

```bash
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --all-languages
```

```zsh
./scripts/test.sh --folder 2167_minimum_time_to_remove_all_cars_containing_illegal_goods --all-languages
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
