# Test harness for 1227_airplane_seat_assignment_probability

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language python
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language javascript
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language typescript
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language java
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language cpp
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language c
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language go
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language rust
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language kotlin
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language swift
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language ruby
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language csharp
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language scala
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language php
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm java java 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm c c 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm go go 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm rust rust 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm swift swift 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm scala scala 1227_airplane_seat_assignment_probability
docker compose -f docker/docker-compose.yml run --rm php php 1227_airplane_seat_assignment_probability
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1227_airplane_seat_assignment_probability` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1227_airplane_seat_assignment_probability` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1227_airplane_seat_assignment_probability` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1227_airplane_seat_assignment_probability` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1227_airplane_seat_assignment_probability` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1227_airplane_seat_assignment_probability` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1227_airplane_seat_assignment_probability` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1227_airplane_seat_assignment_probability` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1227_airplane_seat_assignment_probability` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1227_airplane_seat_assignment_probability` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1227_airplane_seat_assignment_probability` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1227_airplane_seat_assignment_probability` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1227_airplane_seat_assignment_probability` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1227_airplane_seat_assignment_probability` |

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
.\scripts\test.ps1 -Folder 1227_airplane_seat_assignment_probability -AllLanguages
```

```bash
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --all-languages
```

```zsh
./scripts/test.sh --folder 1227_airplane_seat_assignment_probability --all-languages
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
