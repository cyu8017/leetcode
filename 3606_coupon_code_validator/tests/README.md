# Test harness for 3606_coupon_code_validator

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3606_coupon_code_validator -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3606_coupon_code_validator --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3606_coupon_code_validator --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3606_coupon_code_validator --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3606_coupon_code_validator --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3606_coupon_code_validator --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3606_coupon_code_validator --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3606_coupon_code_validator --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3606_coupon_code_validator --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3606_coupon_code_validator --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3606_coupon_code_validator --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3606_coupon_code_validator --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3606_coupon_code_validator --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3606_coupon_code_validator --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3606_coupon_code_validator --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3606_coupon_code_validator --language python
./scripts/test.sh --folder 3606_coupon_code_validator --language javascript
./scripts/test.sh --folder 3606_coupon_code_validator --language typescript
./scripts/test.sh --folder 3606_coupon_code_validator --language java
./scripts/test.sh --folder 3606_coupon_code_validator --language cpp
./scripts/test.sh --folder 3606_coupon_code_validator --language c
./scripts/test.sh --folder 3606_coupon_code_validator --language go
./scripts/test.sh --folder 3606_coupon_code_validator --language rust
./scripts/test.sh --folder 3606_coupon_code_validator --language kotlin
./scripts/test.sh --folder 3606_coupon_code_validator --language swift
./scripts/test.sh --folder 3606_coupon_code_validator --language ruby
./scripts/test.sh --folder 3606_coupon_code_validator --language csharp
./scripts/test.sh --folder 3606_coupon_code_validator --language scala
./scripts/test.sh --folder 3606_coupon_code_validator --language php
./scripts/test.sh --folder 3606_coupon_code_validator --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3606_coupon_code_validator --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3606_coupon_code_validator --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3606_coupon_code_validator --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3606_coupon_code_validator --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3606_coupon_code_validator --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3606_coupon_code_validator --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3606_coupon_code_validator --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3606_coupon_code_validator --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3606_coupon_code_validator --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3606_coupon_code_validator --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3606_coupon_code_validator --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3606_coupon_code_validator --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3606_coupon_code_validator --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3606_coupon_code_validator --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm java java 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm c c 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm go go 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm rust rust 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm swift swift 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm scala scala 3606_coupon_code_validator
docker compose -f docker/docker-compose.yml run --rm php php 3606_coupon_code_validator
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3606_coupon_code_validator` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3606_coupon_code_validator` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3606_coupon_code_validator` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3606_coupon_code_validator` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3606_coupon_code_validator` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3606_coupon_code_validator` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3606_coupon_code_validator` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3606_coupon_code_validator` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3606_coupon_code_validator` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3606_coupon_code_validator` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3606_coupon_code_validator` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3606_coupon_code_validator` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3606_coupon_code_validator` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3606_coupon_code_validator` |

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
.\scripts\test.ps1 -Folder 3606_coupon_code_validator -AllLanguages
```

```bash
./scripts/test.sh --folder 3606_coupon_code_validator --all-languages
```

```zsh
./scripts/test.sh --folder 3606_coupon_code_validator --all-languages
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
