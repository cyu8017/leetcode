# Test harness for 3931_check_adjacent_digit_differences

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language python
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language javascript
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language typescript
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language java
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language cpp
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language c
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language go
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language rust
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language kotlin
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language swift
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language ruby
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language csharp
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language scala
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language php
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3931_check_adjacent_digit_differences --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm java java 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm c c 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm go go 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm rust rust 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm swift swift 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm scala scala 3931_check_adjacent_digit_differences
docker compose -f docker/docker-compose.yml run --rm php php 3931_check_adjacent_digit_differences
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3931_check_adjacent_digit_differences` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3931_check_adjacent_digit_differences` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3931_check_adjacent_digit_differences` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3931_check_adjacent_digit_differences` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3931_check_adjacent_digit_differences` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3931_check_adjacent_digit_differences` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3931_check_adjacent_digit_differences` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3931_check_adjacent_digit_differences` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3931_check_adjacent_digit_differences` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3931_check_adjacent_digit_differences` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3931_check_adjacent_digit_differences` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3931_check_adjacent_digit_differences` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3931_check_adjacent_digit_differences` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3931_check_adjacent_digit_differences` |

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
.\scripts\test.ps1 -Folder 3931_check_adjacent_digit_differences -AllLanguages
```

```bash
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --all-languages
```

```zsh
./scripts/test.sh --folder 3931_check_adjacent_digit_differences --all-languages
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
