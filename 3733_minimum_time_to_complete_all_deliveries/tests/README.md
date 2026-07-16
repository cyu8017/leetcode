# Test harness for 3733_minimum_time_to_complete_all_deliveries

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language python
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language javascript
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language typescript
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language java
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language cpp
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language c
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language go
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language rust
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language kotlin
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language swift
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language ruby
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language csharp
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language scala
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language php
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm java java 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm c c 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm go go 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm rust rust 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm swift swift 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm scala scala 3733_minimum_time_to_complete_all_deliveries
docker compose -f docker/docker-compose.yml run --rm php php 3733_minimum_time_to_complete_all_deliveries
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3733_minimum_time_to_complete_all_deliveries` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3733_minimum_time_to_complete_all_deliveries` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3733_minimum_time_to_complete_all_deliveries` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3733_minimum_time_to_complete_all_deliveries` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3733_minimum_time_to_complete_all_deliveries` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3733_minimum_time_to_complete_all_deliveries` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3733_minimum_time_to_complete_all_deliveries` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3733_minimum_time_to_complete_all_deliveries` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3733_minimum_time_to_complete_all_deliveries` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3733_minimum_time_to_complete_all_deliveries` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3733_minimum_time_to_complete_all_deliveries` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3733_minimum_time_to_complete_all_deliveries` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3733_minimum_time_to_complete_all_deliveries` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3733_minimum_time_to_complete_all_deliveries` |

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
.\scripts\test.ps1 -Folder 3733_minimum_time_to_complete_all_deliveries -AllLanguages
```

```bash
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --all-languages
```

```zsh
./scripts/test.sh --folder 3733_minimum_time_to_complete_all_deliveries --all-languages
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
