# Test harness for 2020_number_of_accounts_that_did_not_stream

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language python
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language javascript
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language typescript
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language java
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language cpp
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language c
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language go
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language rust
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language kotlin
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language swift
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language ruby
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language csharp
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language scala
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language php
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm java java 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm c c 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm go go 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm rust rust 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm swift swift 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm scala scala 2020_number_of_accounts_that_did_not_stream
docker compose -f docker/docker-compose.yml run --rm php php 2020_number_of_accounts_that_did_not_stream
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2020_number_of_accounts_that_did_not_stream` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2020_number_of_accounts_that_did_not_stream` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2020_number_of_accounts_that_did_not_stream` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2020_number_of_accounts_that_did_not_stream` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2020_number_of_accounts_that_did_not_stream` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2020_number_of_accounts_that_did_not_stream` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2020_number_of_accounts_that_did_not_stream` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2020_number_of_accounts_that_did_not_stream` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2020_number_of_accounts_that_did_not_stream` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2020_number_of_accounts_that_did_not_stream` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2020_number_of_accounts_that_did_not_stream` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2020_number_of_accounts_that_did_not_stream` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2020_number_of_accounts_that_did_not_stream` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2020_number_of_accounts_that_did_not_stream` |

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
.\scripts\test.ps1 -Folder 2020_number_of_accounts_that_did_not_stream -AllLanguages
```

```bash
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --all-languages
```

```zsh
./scripts/test.sh --folder 2020_number_of_accounts_that_did_not_stream --all-languages
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
