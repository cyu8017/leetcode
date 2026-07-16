# Test harness for 1109_corporate_flight_bookings

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1109_corporate_flight_bookings --language python
./scripts/test.sh --folder 1109_corporate_flight_bookings --language javascript
./scripts/test.sh --folder 1109_corporate_flight_bookings --language typescript
./scripts/test.sh --folder 1109_corporate_flight_bookings --language java
./scripts/test.sh --folder 1109_corporate_flight_bookings --language cpp
./scripts/test.sh --folder 1109_corporate_flight_bookings --language c
./scripts/test.sh --folder 1109_corporate_flight_bookings --language go
./scripts/test.sh --folder 1109_corporate_flight_bookings --language rust
./scripts/test.sh --folder 1109_corporate_flight_bookings --language kotlin
./scripts/test.sh --folder 1109_corporate_flight_bookings --language swift
./scripts/test.sh --folder 1109_corporate_flight_bookings --language ruby
./scripts/test.sh --folder 1109_corporate_flight_bookings --language csharp
./scripts/test.sh --folder 1109_corporate_flight_bookings --language scala
./scripts/test.sh --folder 1109_corporate_flight_bookings --language php
./scripts/test.sh --folder 1109_corporate_flight_bookings --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1109_corporate_flight_bookings --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm java java 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm c c 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm go go 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm rust rust 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm swift swift 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm scala scala 1109_corporate_flight_bookings
docker compose -f docker/docker-compose.yml run --rm php php 1109_corporate_flight_bookings
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1109_corporate_flight_bookings` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1109_corporate_flight_bookings` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1109_corporate_flight_bookings` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1109_corporate_flight_bookings` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1109_corporate_flight_bookings` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1109_corporate_flight_bookings` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1109_corporate_flight_bookings` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1109_corporate_flight_bookings` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1109_corporate_flight_bookings` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1109_corporate_flight_bookings` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1109_corporate_flight_bookings` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1109_corporate_flight_bookings` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1109_corporate_flight_bookings` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1109_corporate_flight_bookings` |

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
.\scripts\test.ps1 -Folder 1109_corporate_flight_bookings -AllLanguages
```

```bash
./scripts/test.sh --folder 1109_corporate_flight_bookings --all-languages
```

```zsh
./scripts/test.sh --folder 1109_corporate_flight_bookings --all-languages
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
