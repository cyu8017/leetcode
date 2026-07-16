# Test harness for 3601_find_drivers_with_improved_fuel_efficiency

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language python
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language javascript
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language typescript
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language java
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language cpp
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language c
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language go
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language rust
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language kotlin
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language swift
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language ruby
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language csharp
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language scala
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language php
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm java java 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm c c 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm go go 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm rust rust 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm swift swift 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm scala scala 3601_find_drivers_with_improved_fuel_efficiency
docker compose -f docker/docker-compose.yml run --rm php php 3601_find_drivers_with_improved_fuel_efficiency
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3601_find_drivers_with_improved_fuel_efficiency` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3601_find_drivers_with_improved_fuel_efficiency` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3601_find_drivers_with_improved_fuel_efficiency` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3601_find_drivers_with_improved_fuel_efficiency` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3601_find_drivers_with_improved_fuel_efficiency` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3601_find_drivers_with_improved_fuel_efficiency` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3601_find_drivers_with_improved_fuel_efficiency` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3601_find_drivers_with_improved_fuel_efficiency` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3601_find_drivers_with_improved_fuel_efficiency` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3601_find_drivers_with_improved_fuel_efficiency` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3601_find_drivers_with_improved_fuel_efficiency` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3601_find_drivers_with_improved_fuel_efficiency` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3601_find_drivers_with_improved_fuel_efficiency` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3601_find_drivers_with_improved_fuel_efficiency` |

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
.\scripts\test.ps1 -Folder 3601_find_drivers_with_improved_fuel_efficiency -AllLanguages
```

```bash
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --all-languages
```

```zsh
./scripts/test.sh --folder 3601_find_drivers_with_improved_fuel_efficiency --all-languages
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
