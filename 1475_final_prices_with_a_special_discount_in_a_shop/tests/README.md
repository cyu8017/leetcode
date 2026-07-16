# Test harness for 1475_final_prices_with_a_special_discount_in_a_shop

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language python
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language javascript
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language typescript
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language java
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language cpp
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language c
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language go
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language rust
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language kotlin
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language swift
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language ruby
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language csharp
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language scala
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language php
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm java java 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm c c 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm go go 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm rust rust 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm swift swift 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm scala scala 1475_final_prices_with_a_special_discount_in_a_shop
docker compose -f docker/docker-compose.yml run --rm php php 1475_final_prices_with_a_special_discount_in_a_shop
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1475_final_prices_with_a_special_discount_in_a_shop` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1475_final_prices_with_a_special_discount_in_a_shop` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1475_final_prices_with_a_special_discount_in_a_shop` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1475_final_prices_with_a_special_discount_in_a_shop` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1475_final_prices_with_a_special_discount_in_a_shop` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1475_final_prices_with_a_special_discount_in_a_shop` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1475_final_prices_with_a_special_discount_in_a_shop` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1475_final_prices_with_a_special_discount_in_a_shop` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1475_final_prices_with_a_special_discount_in_a_shop` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1475_final_prices_with_a_special_discount_in_a_shop` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1475_final_prices_with_a_special_discount_in_a_shop` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1475_final_prices_with_a_special_discount_in_a_shop` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1475_final_prices_with_a_special_discount_in_a_shop` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1475_final_prices_with_a_special_discount_in_a_shop` |

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
.\scripts\test.ps1 -Folder 1475_final_prices_with_a_special_discount_in_a_shop -AllLanguages
```

```bash
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --all-languages
```

```zsh
./scripts/test.sh --folder 1475_final_prices_with_a_special_discount_in_a_shop --all-languages
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
