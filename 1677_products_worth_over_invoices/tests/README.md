# Test harness for 1677_products_worth_over_invoices

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1677_products_worth_over_invoices --language python
./scripts/test.sh --folder 1677_products_worth_over_invoices --language javascript
./scripts/test.sh --folder 1677_products_worth_over_invoices --language typescript
./scripts/test.sh --folder 1677_products_worth_over_invoices --language java
./scripts/test.sh --folder 1677_products_worth_over_invoices --language cpp
./scripts/test.sh --folder 1677_products_worth_over_invoices --language c
./scripts/test.sh --folder 1677_products_worth_over_invoices --language go
./scripts/test.sh --folder 1677_products_worth_over_invoices --language rust
./scripts/test.sh --folder 1677_products_worth_over_invoices --language kotlin
./scripts/test.sh --folder 1677_products_worth_over_invoices --language swift
./scripts/test.sh --folder 1677_products_worth_over_invoices --language ruby
./scripts/test.sh --folder 1677_products_worth_over_invoices --language csharp
./scripts/test.sh --folder 1677_products_worth_over_invoices --language scala
./scripts/test.sh --folder 1677_products_worth_over_invoices --language php
./scripts/test.sh --folder 1677_products_worth_over_invoices --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1677_products_worth_over_invoices --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm java java 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm c c 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm go go 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm rust rust 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm swift swift 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm scala scala 1677_products_worth_over_invoices
docker compose -f docker/docker-compose.yml run --rm php php 1677_products_worth_over_invoices
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1677_products_worth_over_invoices` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1677_products_worth_over_invoices` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1677_products_worth_over_invoices` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1677_products_worth_over_invoices` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1677_products_worth_over_invoices` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1677_products_worth_over_invoices` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1677_products_worth_over_invoices` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1677_products_worth_over_invoices` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1677_products_worth_over_invoices` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1677_products_worth_over_invoices` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1677_products_worth_over_invoices` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1677_products_worth_over_invoices` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1677_products_worth_over_invoices` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1677_products_worth_over_invoices` |

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
.\scripts\test.ps1 -Folder 1677_products_worth_over_invoices -AllLanguages
```

```bash
./scripts/test.sh --folder 1677_products_worth_over_invoices --all-languages
```

```zsh
./scripts/test.sh --folder 1677_products_worth_over_invoices --all-languages
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
