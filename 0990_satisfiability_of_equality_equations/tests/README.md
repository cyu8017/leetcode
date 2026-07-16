# Test harness for 0990_satisfiability_of_equality_equations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language python
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language javascript
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language typescript
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language java
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language cpp
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language c
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language go
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language rust
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language kotlin
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language swift
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language ruby
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language csharp
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language scala
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language php
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm java java 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm c c 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm go go 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm rust rust 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm swift swift 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm scala scala 0990_satisfiability_of_equality_equations
docker compose -f docker/docker-compose.yml run --rm php php 0990_satisfiability_of_equality_equations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0990_satisfiability_of_equality_equations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0990_satisfiability_of_equality_equations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0990_satisfiability_of_equality_equations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0990_satisfiability_of_equality_equations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0990_satisfiability_of_equality_equations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0990_satisfiability_of_equality_equations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0990_satisfiability_of_equality_equations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0990_satisfiability_of_equality_equations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0990_satisfiability_of_equality_equations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0990_satisfiability_of_equality_equations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0990_satisfiability_of_equality_equations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0990_satisfiability_of_equality_equations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0990_satisfiability_of_equality_equations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0990_satisfiability_of_equality_equations` |

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
.\scripts\test.ps1 -Folder 0990_satisfiability_of_equality_equations -AllLanguages
```

```bash
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --all-languages
```

```zsh
./scripts/test.sh --folder 0990_satisfiability_of_equality_equations --all-languages
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
