# Test harness for 2232_minimize_result_by_adding_parentheses_to_expression

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language python
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language javascript
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language typescript
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language java
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language cpp
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language c
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language go
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language rust
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language kotlin
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language swift
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language ruby
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language csharp
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language scala
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language php
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm java java 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm c c 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm go go 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm rust rust 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm swift swift 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm scala scala 2232_minimize_result_by_adding_parentheses_to_expression
docker compose -f docker/docker-compose.yml run --rm php php 2232_minimize_result_by_adding_parentheses_to_expression
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2232_minimize_result_by_adding_parentheses_to_expression` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2232_minimize_result_by_adding_parentheses_to_expression` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2232_minimize_result_by_adding_parentheses_to_expression` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2232_minimize_result_by_adding_parentheses_to_expression` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2232_minimize_result_by_adding_parentheses_to_expression` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2232_minimize_result_by_adding_parentheses_to_expression` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2232_minimize_result_by_adding_parentheses_to_expression` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2232_minimize_result_by_adding_parentheses_to_expression` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2232_minimize_result_by_adding_parentheses_to_expression` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2232_minimize_result_by_adding_parentheses_to_expression` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2232_minimize_result_by_adding_parentheses_to_expression` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2232_minimize_result_by_adding_parentheses_to_expression` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2232_minimize_result_by_adding_parentheses_to_expression` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2232_minimize_result_by_adding_parentheses_to_expression` |

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
.\scripts\test.ps1 -Folder 2232_minimize_result_by_adding_parentheses_to_expression -AllLanguages
```

```bash
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --all-languages
```

```zsh
./scripts/test.sh --folder 2232_minimize_result_by_adding_parentheses_to_expression --all-languages
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
