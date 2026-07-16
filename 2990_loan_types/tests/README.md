# Test harness for 2990_loan_types

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2990_loan_types -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2990_loan_types --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2990_loan_types --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2990_loan_types --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2990_loan_types --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2990_loan_types --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2990_loan_types --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2990_loan_types --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2990_loan_types --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2990_loan_types --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2990_loan_types --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2990_loan_types --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2990_loan_types --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2990_loan_types --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2990_loan_types --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2990_loan_types --language python
./scripts/test.sh --folder 2990_loan_types --language javascript
./scripts/test.sh --folder 2990_loan_types --language typescript
./scripts/test.sh --folder 2990_loan_types --language java
./scripts/test.sh --folder 2990_loan_types --language cpp
./scripts/test.sh --folder 2990_loan_types --language c
./scripts/test.sh --folder 2990_loan_types --language go
./scripts/test.sh --folder 2990_loan_types --language rust
./scripts/test.sh --folder 2990_loan_types --language kotlin
./scripts/test.sh --folder 2990_loan_types --language swift
./scripts/test.sh --folder 2990_loan_types --language ruby
./scripts/test.sh --folder 2990_loan_types --language csharp
./scripts/test.sh --folder 2990_loan_types --language scala
./scripts/test.sh --folder 2990_loan_types --language php
./scripts/test.sh --folder 2990_loan_types --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2990_loan_types --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2990_loan_types --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2990_loan_types --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2990_loan_types --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2990_loan_types --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2990_loan_types --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2990_loan_types --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2990_loan_types --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2990_loan_types --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2990_loan_types --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2990_loan_types --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2990_loan_types --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2990_loan_types --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2990_loan_types --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm java java 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm c c 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm go go 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm rust rust 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm swift swift 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm scala scala 2990_loan_types
docker compose -f docker/docker-compose.yml run --rm php php 2990_loan_types
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2990_loan_types` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2990_loan_types` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2990_loan_types` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2990_loan_types` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2990_loan_types` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2990_loan_types` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2990_loan_types` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2990_loan_types` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2990_loan_types` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2990_loan_types` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2990_loan_types` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2990_loan_types` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2990_loan_types` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2990_loan_types` |

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
.\scripts\test.ps1 -Folder 2990_loan_types -AllLanguages
```

```bash
./scripts/test.sh --folder 2990_loan_types --all-languages
```

```zsh
./scripts/test.sh --folder 2990_loan_types --all-languages
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
