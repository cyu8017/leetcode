# Test harness for 0774_minimize_max_distance_to_gas_station

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language python
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language javascript
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language typescript
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language java
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language cpp
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language c
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language go
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language rust
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language kotlin
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language swift
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language ruby
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language csharp
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language scala
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language php
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm java java 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm c c 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm go go 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm rust rust 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm swift swift 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm scala scala 0774_minimize_max_distance_to_gas_station
docker compose -f docker/docker-compose.yml run --rm php php 0774_minimize_max_distance_to_gas_station
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0774_minimize_max_distance_to_gas_station` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0774_minimize_max_distance_to_gas_station` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0774_minimize_max_distance_to_gas_station` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0774_minimize_max_distance_to_gas_station` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0774_minimize_max_distance_to_gas_station` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0774_minimize_max_distance_to_gas_station` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0774_minimize_max_distance_to_gas_station` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0774_minimize_max_distance_to_gas_station` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0774_minimize_max_distance_to_gas_station` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0774_minimize_max_distance_to_gas_station` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0774_minimize_max_distance_to_gas_station` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0774_minimize_max_distance_to_gas_station` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0774_minimize_max_distance_to_gas_station` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0774_minimize_max_distance_to_gas_station` |

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
.\scripts\test.ps1 -Folder 0774_minimize_max_distance_to_gas_station -AllLanguages
```

```bash
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --all-languages
```

```zsh
./scripts/test.sh --folder 0774_minimize_max_distance_to_gas_station --all-languages
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
