# Test harness for 0439_ternary_expression_parser

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0439_ternary_expression_parser --language python
./scripts/test.sh --folder 0439_ternary_expression_parser --language javascript
./scripts/test.sh --folder 0439_ternary_expression_parser --language typescript
./scripts/test.sh --folder 0439_ternary_expression_parser --language java
./scripts/test.sh --folder 0439_ternary_expression_parser --language cpp
./scripts/test.sh --folder 0439_ternary_expression_parser --language c
./scripts/test.sh --folder 0439_ternary_expression_parser --language go
./scripts/test.sh --folder 0439_ternary_expression_parser --language rust
./scripts/test.sh --folder 0439_ternary_expression_parser --language kotlin
./scripts/test.sh --folder 0439_ternary_expression_parser --language swift
./scripts/test.sh --folder 0439_ternary_expression_parser --language ruby
./scripts/test.sh --folder 0439_ternary_expression_parser --language csharp
./scripts/test.sh --folder 0439_ternary_expression_parser --language scala
./scripts/test.sh --folder 0439_ternary_expression_parser --language php
./scripts/test.sh --folder 0439_ternary_expression_parser --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0439_ternary_expression_parser --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm java java 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm c c 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm go go 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm rust rust 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm swift swift 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm scala scala 0439_ternary_expression_parser
docker compose -f docker/docker-compose.yml run --rm php php 0439_ternary_expression_parser
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0439_ternary_expression_parser` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0439_ternary_expression_parser` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0439_ternary_expression_parser` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0439_ternary_expression_parser` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0439_ternary_expression_parser` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0439_ternary_expression_parser` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0439_ternary_expression_parser` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0439_ternary_expression_parser` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0439_ternary_expression_parser` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0439_ternary_expression_parser` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0439_ternary_expression_parser` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0439_ternary_expression_parser` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0439_ternary_expression_parser` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0439_ternary_expression_parser` |

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
.\scripts\test.ps1 -Folder 0439_ternary_expression_parser -AllLanguages
```

```bash
./scripts/test.sh --folder 0439_ternary_expression_parser --all-languages
```

```zsh
./scripts/test.sh --folder 0439_ternary_expression_parser --all-languages
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
