# Test harness for 0603_consecutive_available_seats

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0603_consecutive_available_seats --language python
./scripts/test.sh --folder 0603_consecutive_available_seats --language javascript
./scripts/test.sh --folder 0603_consecutive_available_seats --language typescript
./scripts/test.sh --folder 0603_consecutive_available_seats --language java
./scripts/test.sh --folder 0603_consecutive_available_seats --language cpp
./scripts/test.sh --folder 0603_consecutive_available_seats --language c
./scripts/test.sh --folder 0603_consecutive_available_seats --language go
./scripts/test.sh --folder 0603_consecutive_available_seats --language rust
./scripts/test.sh --folder 0603_consecutive_available_seats --language kotlin
./scripts/test.sh --folder 0603_consecutive_available_seats --language swift
./scripts/test.sh --folder 0603_consecutive_available_seats --language ruby
./scripts/test.sh --folder 0603_consecutive_available_seats --language csharp
./scripts/test.sh --folder 0603_consecutive_available_seats --language scala
./scripts/test.sh --folder 0603_consecutive_available_seats --language php
./scripts/test.sh --folder 0603_consecutive_available_seats --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0603_consecutive_available_seats --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm java java 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm c c 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm go go 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm rust rust 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm swift swift 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm scala scala 0603_consecutive_available_seats
docker compose -f docker/docker-compose.yml run --rm php php 0603_consecutive_available_seats
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0603_consecutive_available_seats` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0603_consecutive_available_seats` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0603_consecutive_available_seats` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0603_consecutive_available_seats` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0603_consecutive_available_seats` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0603_consecutive_available_seats` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0603_consecutive_available_seats` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0603_consecutive_available_seats` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0603_consecutive_available_seats` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0603_consecutive_available_seats` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0603_consecutive_available_seats` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0603_consecutive_available_seats` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0603_consecutive_available_seats` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0603_consecutive_available_seats` |

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
.\scripts\test.ps1 -Folder 0603_consecutive_available_seats -AllLanguages
```

```bash
./scripts/test.sh --folder 0603_consecutive_available_seats --all-languages
```

```zsh
./scripts/test.sh --folder 0603_consecutive_available_seats --all-languages
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
