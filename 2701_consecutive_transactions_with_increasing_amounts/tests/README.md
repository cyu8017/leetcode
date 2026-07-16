# Test harness for 2701_consecutive_transactions_with_increasing_amounts

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language python
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language javascript
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language typescript
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language java
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language cpp
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language c
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language go
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language rust
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language kotlin
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language swift
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language ruby
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language csharp
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language scala
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language php
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm java java 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm c c 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm go go 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm rust rust 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm swift swift 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm scala scala 2701_consecutive_transactions_with_increasing_amounts
docker compose -f docker/docker-compose.yml run --rm php php 2701_consecutive_transactions_with_increasing_amounts
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2701_consecutive_transactions_with_increasing_amounts` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2701_consecutive_transactions_with_increasing_amounts` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2701_consecutive_transactions_with_increasing_amounts` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2701_consecutive_transactions_with_increasing_amounts` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2701_consecutive_transactions_with_increasing_amounts` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2701_consecutive_transactions_with_increasing_amounts` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2701_consecutive_transactions_with_increasing_amounts` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2701_consecutive_transactions_with_increasing_amounts` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2701_consecutive_transactions_with_increasing_amounts` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2701_consecutive_transactions_with_increasing_amounts` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2701_consecutive_transactions_with_increasing_amounts` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2701_consecutive_transactions_with_increasing_amounts` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2701_consecutive_transactions_with_increasing_amounts` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2701_consecutive_transactions_with_increasing_amounts` |

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
.\scripts\test.ps1 -Folder 2701_consecutive_transactions_with_increasing_amounts -AllLanguages
```

```bash
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --all-languages
```

```zsh
./scripts/test.sh --folder 2701_consecutive_transactions_with_increasing_amounts --all-languages
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
