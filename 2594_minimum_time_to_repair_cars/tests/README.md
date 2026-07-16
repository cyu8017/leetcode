# Test harness for 2594_minimum_time_to_repair_cars

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language python
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language javascript
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language typescript
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language java
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language cpp
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language c
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language go
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language rust
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language kotlin
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language swift
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language ruby
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language csharp
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language scala
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language php
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm java java 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm c c 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm go go 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm rust rust 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm swift swift 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm scala scala 2594_minimum_time_to_repair_cars
docker compose -f docker/docker-compose.yml run --rm php php 2594_minimum_time_to_repair_cars
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2594_minimum_time_to_repair_cars` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2594_minimum_time_to_repair_cars` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2594_minimum_time_to_repair_cars` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2594_minimum_time_to_repair_cars` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2594_minimum_time_to_repair_cars` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2594_minimum_time_to_repair_cars` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2594_minimum_time_to_repair_cars` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2594_minimum_time_to_repair_cars` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2594_minimum_time_to_repair_cars` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2594_minimum_time_to_repair_cars` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2594_minimum_time_to_repair_cars` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2594_minimum_time_to_repair_cars` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2594_minimum_time_to_repair_cars` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2594_minimum_time_to_repair_cars` |

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
.\scripts\test.ps1 -Folder 2594_minimum_time_to_repair_cars -AllLanguages
```

```bash
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --all-languages
```

```zsh
./scripts/test.sh --folder 2594_minimum_time_to_repair_cars --all-languages
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
