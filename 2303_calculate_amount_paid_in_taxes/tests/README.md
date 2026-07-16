# Test harness for 2303_calculate_amount_paid_in_taxes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language python
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language javascript
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language typescript
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language java
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language cpp
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language c
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language go
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language rust
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language kotlin
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language swift
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language ruby
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language csharp
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language scala
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language php
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm java java 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm c c 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm go go 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm rust rust 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm swift swift 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm scala scala 2303_calculate_amount_paid_in_taxes
docker compose -f docker/docker-compose.yml run --rm php php 2303_calculate_amount_paid_in_taxes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2303_calculate_amount_paid_in_taxes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2303_calculate_amount_paid_in_taxes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2303_calculate_amount_paid_in_taxes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2303_calculate_amount_paid_in_taxes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2303_calculate_amount_paid_in_taxes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2303_calculate_amount_paid_in_taxes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2303_calculate_amount_paid_in_taxes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2303_calculate_amount_paid_in_taxes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2303_calculate_amount_paid_in_taxes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2303_calculate_amount_paid_in_taxes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2303_calculate_amount_paid_in_taxes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2303_calculate_amount_paid_in_taxes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2303_calculate_amount_paid_in_taxes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2303_calculate_amount_paid_in_taxes` |

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
.\scripts\test.ps1 -Folder 2303_calculate_amount_paid_in_taxes -AllLanguages
```

```bash
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --all-languages
```

```zsh
./scripts/test.sh --folder 2303_calculate_amount_paid_in_taxes --all-languages
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
