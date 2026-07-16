# Test harness for 1946_largest_number_after_mutating_substring

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language python
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language javascript
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language typescript
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language java
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language cpp
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language c
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language go
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language rust
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language kotlin
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language swift
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language ruby
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language csharp
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language scala
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language php
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm java java 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm c c 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm go go 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm rust rust 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm swift swift 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm scala scala 1946_largest_number_after_mutating_substring
docker compose -f docker/docker-compose.yml run --rm php php 1946_largest_number_after_mutating_substring
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1946_largest_number_after_mutating_substring` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1946_largest_number_after_mutating_substring` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1946_largest_number_after_mutating_substring` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1946_largest_number_after_mutating_substring` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1946_largest_number_after_mutating_substring` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1946_largest_number_after_mutating_substring` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1946_largest_number_after_mutating_substring` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1946_largest_number_after_mutating_substring` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1946_largest_number_after_mutating_substring` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1946_largest_number_after_mutating_substring` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1946_largest_number_after_mutating_substring` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1946_largest_number_after_mutating_substring` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1946_largest_number_after_mutating_substring` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1946_largest_number_after_mutating_substring` |

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
.\scripts\test.ps1 -Folder 1946_largest_number_after_mutating_substring -AllLanguages
```

```bash
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --all-languages
```

```zsh
./scripts/test.sh --folder 1946_largest_number_after_mutating_substring --all-languages
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
