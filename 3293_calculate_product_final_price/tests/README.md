# Test harness for 3293_calculate_product_final_price

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3293_calculate_product_final_price --language python
./scripts/test.sh --folder 3293_calculate_product_final_price --language javascript
./scripts/test.sh --folder 3293_calculate_product_final_price --language typescript
./scripts/test.sh --folder 3293_calculate_product_final_price --language java
./scripts/test.sh --folder 3293_calculate_product_final_price --language cpp
./scripts/test.sh --folder 3293_calculate_product_final_price --language c
./scripts/test.sh --folder 3293_calculate_product_final_price --language go
./scripts/test.sh --folder 3293_calculate_product_final_price --language rust
./scripts/test.sh --folder 3293_calculate_product_final_price --language kotlin
./scripts/test.sh --folder 3293_calculate_product_final_price --language swift
./scripts/test.sh --folder 3293_calculate_product_final_price --language ruby
./scripts/test.sh --folder 3293_calculate_product_final_price --language csharp
./scripts/test.sh --folder 3293_calculate_product_final_price --language scala
./scripts/test.sh --folder 3293_calculate_product_final_price --language php
./scripts/test.sh --folder 3293_calculate_product_final_price --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3293_calculate_product_final_price --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm java java 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm c c 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm go go 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm rust rust 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm swift swift 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm scala scala 3293_calculate_product_final_price
docker compose -f docker/docker-compose.yml run --rm php php 3293_calculate_product_final_price
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3293_calculate_product_final_price` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3293_calculate_product_final_price` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3293_calculate_product_final_price` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3293_calculate_product_final_price` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3293_calculate_product_final_price` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3293_calculate_product_final_price` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3293_calculate_product_final_price` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3293_calculate_product_final_price` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3293_calculate_product_final_price` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3293_calculate_product_final_price` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3293_calculate_product_final_price` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3293_calculate_product_final_price` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3293_calculate_product_final_price` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3293_calculate_product_final_price` |

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
.\scripts\test.ps1 -Folder 3293_calculate_product_final_price -AllLanguages
```

```bash
./scripts/test.sh --folder 3293_calculate_product_final_price --all-languages
```

```zsh
./scripts/test.sh --folder 3293_calculate_product_final_price --all-languages
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
