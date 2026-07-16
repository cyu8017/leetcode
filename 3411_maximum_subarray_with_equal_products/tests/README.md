# Test harness for 3411_maximum_subarray_with_equal_products

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language python
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language javascript
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language typescript
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language java
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language cpp
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language c
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language go
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language rust
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language kotlin
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language swift
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language ruby
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language csharp
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language scala
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language php
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm java java 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm c c 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm go go 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm rust rust 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm swift swift 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm scala scala 3411_maximum_subarray_with_equal_products
docker compose -f docker/docker-compose.yml run --rm php php 3411_maximum_subarray_with_equal_products
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3411_maximum_subarray_with_equal_products` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3411_maximum_subarray_with_equal_products` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3411_maximum_subarray_with_equal_products` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3411_maximum_subarray_with_equal_products` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3411_maximum_subarray_with_equal_products` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3411_maximum_subarray_with_equal_products` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3411_maximum_subarray_with_equal_products` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3411_maximum_subarray_with_equal_products` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3411_maximum_subarray_with_equal_products` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3411_maximum_subarray_with_equal_products` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3411_maximum_subarray_with_equal_products` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3411_maximum_subarray_with_equal_products` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3411_maximum_subarray_with_equal_products` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3411_maximum_subarray_with_equal_products` |

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
.\scripts\test.ps1 -Folder 3411_maximum_subarray_with_equal_products -AllLanguages
```

```bash
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --all-languages
```

```zsh
./scripts/test.sh --folder 3411_maximum_subarray_with_equal_products --all-languages
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
