# Test harness for 3448_count_substrings_divisible_by_last_digit

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language python
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language javascript
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language typescript
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language java
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language cpp
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language c
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language go
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language rust
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language kotlin
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language swift
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language ruby
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language csharp
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language scala
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language php
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm java java 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm c c 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm go go 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm rust rust 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm swift swift 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm scala scala 3448_count_substrings_divisible_by_last_digit
docker compose -f docker/docker-compose.yml run --rm php php 3448_count_substrings_divisible_by_last_digit
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3448_count_substrings_divisible_by_last_digit` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3448_count_substrings_divisible_by_last_digit` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3448_count_substrings_divisible_by_last_digit` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3448_count_substrings_divisible_by_last_digit` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3448_count_substrings_divisible_by_last_digit` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3448_count_substrings_divisible_by_last_digit` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3448_count_substrings_divisible_by_last_digit` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3448_count_substrings_divisible_by_last_digit` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3448_count_substrings_divisible_by_last_digit` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3448_count_substrings_divisible_by_last_digit` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3448_count_substrings_divisible_by_last_digit` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3448_count_substrings_divisible_by_last_digit` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3448_count_substrings_divisible_by_last_digit` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3448_count_substrings_divisible_by_last_digit` |

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
.\scripts\test.ps1 -Folder 3448_count_substrings_divisible_by_last_digit -AllLanguages
```

```bash
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --all-languages
```

```zsh
./scripts/test.sh --folder 3448_count_substrings_divisible_by_last_digit --all-languages
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
