# Test harness for 2604_minimum_time_to_eat_all_grains

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language python
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language javascript
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language typescript
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language java
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language cpp
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language c
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language go
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language rust
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language kotlin
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language swift
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language ruby
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language csharp
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language scala
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language php
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm java java 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm c c 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm go go 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm rust rust 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm swift swift 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm scala scala 2604_minimum_time_to_eat_all_grains
docker compose -f docker/docker-compose.yml run --rm php php 2604_minimum_time_to_eat_all_grains
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2604_minimum_time_to_eat_all_grains` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2604_minimum_time_to_eat_all_grains` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2604_minimum_time_to_eat_all_grains` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2604_minimum_time_to_eat_all_grains` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2604_minimum_time_to_eat_all_grains` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2604_minimum_time_to_eat_all_grains` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2604_minimum_time_to_eat_all_grains` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2604_minimum_time_to_eat_all_grains` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2604_minimum_time_to_eat_all_grains` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2604_minimum_time_to_eat_all_grains` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2604_minimum_time_to_eat_all_grains` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2604_minimum_time_to_eat_all_grains` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2604_minimum_time_to_eat_all_grains` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2604_minimum_time_to_eat_all_grains` |

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
.\scripts\test.ps1 -Folder 2604_minimum_time_to_eat_all_grains -AllLanguages
```

```bash
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --all-languages
```

```zsh
./scripts/test.sh --folder 2604_minimum_time_to_eat_all_grains --all-languages
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
