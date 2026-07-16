# Test harness for 2534_time_taken_to_cross_the_door

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language python
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language javascript
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language typescript
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language java
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language cpp
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language c
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language go
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language rust
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language kotlin
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language swift
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language ruby
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language csharp
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language scala
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language php
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm java java 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm c c 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm go go 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm rust rust 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm swift swift 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm scala scala 2534_time_taken_to_cross_the_door
docker compose -f docker/docker-compose.yml run --rm php php 2534_time_taken_to_cross_the_door
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2534_time_taken_to_cross_the_door` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2534_time_taken_to_cross_the_door` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2534_time_taken_to_cross_the_door` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2534_time_taken_to_cross_the_door` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2534_time_taken_to_cross_the_door` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2534_time_taken_to_cross_the_door` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2534_time_taken_to_cross_the_door` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2534_time_taken_to_cross_the_door` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2534_time_taken_to_cross_the_door` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2534_time_taken_to_cross_the_door` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2534_time_taken_to_cross_the_door` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2534_time_taken_to_cross_the_door` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2534_time_taken_to_cross_the_door` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2534_time_taken_to_cross_the_door` |

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
.\scripts\test.ps1 -Folder 2534_time_taken_to_cross_the_door -AllLanguages
```

```bash
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --all-languages
```

```zsh
./scripts/test.sh --folder 2534_time_taken_to_cross_the_door --all-languages
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
