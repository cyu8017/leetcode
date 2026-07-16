# Test harness for 0853_car_fleet

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0853_car_fleet -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0853_car_fleet --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0853_car_fleet --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0853_car_fleet --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0853_car_fleet --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0853_car_fleet --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0853_car_fleet --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0853_car_fleet --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0853_car_fleet --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0853_car_fleet --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0853_car_fleet --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0853_car_fleet --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0853_car_fleet --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0853_car_fleet --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0853_car_fleet --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0853_car_fleet --language python
./scripts/test.sh --folder 0853_car_fleet --language javascript
./scripts/test.sh --folder 0853_car_fleet --language typescript
./scripts/test.sh --folder 0853_car_fleet --language java
./scripts/test.sh --folder 0853_car_fleet --language cpp
./scripts/test.sh --folder 0853_car_fleet --language c
./scripts/test.sh --folder 0853_car_fleet --language go
./scripts/test.sh --folder 0853_car_fleet --language rust
./scripts/test.sh --folder 0853_car_fleet --language kotlin
./scripts/test.sh --folder 0853_car_fleet --language swift
./scripts/test.sh --folder 0853_car_fleet --language ruby
./scripts/test.sh --folder 0853_car_fleet --language csharp
./scripts/test.sh --folder 0853_car_fleet --language scala
./scripts/test.sh --folder 0853_car_fleet --language php
./scripts/test.sh --folder 0853_car_fleet --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0853_car_fleet --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0853_car_fleet --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0853_car_fleet --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0853_car_fleet --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0853_car_fleet --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0853_car_fleet --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0853_car_fleet --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0853_car_fleet --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0853_car_fleet --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0853_car_fleet --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0853_car_fleet --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0853_car_fleet --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0853_car_fleet --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0853_car_fleet --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm java java 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm c c 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm go go 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm rust rust 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm swift swift 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm scala scala 0853_car_fleet
docker compose -f docker/docker-compose.yml run --rm php php 0853_car_fleet
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0853_car_fleet` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0853_car_fleet` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0853_car_fleet` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0853_car_fleet` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0853_car_fleet` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0853_car_fleet` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0853_car_fleet` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0853_car_fleet` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0853_car_fleet` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0853_car_fleet` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0853_car_fleet` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0853_car_fleet` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0853_car_fleet` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0853_car_fleet` |

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
.\scripts\test.ps1 -Folder 0853_car_fleet -AllLanguages
```

```bash
./scripts/test.sh --folder 0853_car_fleet --all-languages
```

```zsh
./scripts/test.sh --folder 0853_car_fleet --all-languages
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
