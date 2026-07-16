# Test harness for 2233_maximum_product_after_k_increments

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language python
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language javascript
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language typescript
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language java
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language cpp
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language c
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language go
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language rust
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language kotlin
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language swift
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language ruby
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language csharp
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language scala
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language php
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2233_maximum_product_after_k_increments --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm java java 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm c c 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm go go 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm rust rust 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm swift swift 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm scala scala 2233_maximum_product_after_k_increments
docker compose -f docker/docker-compose.yml run --rm php php 2233_maximum_product_after_k_increments
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2233_maximum_product_after_k_increments` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2233_maximum_product_after_k_increments` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2233_maximum_product_after_k_increments` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2233_maximum_product_after_k_increments` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2233_maximum_product_after_k_increments` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2233_maximum_product_after_k_increments` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2233_maximum_product_after_k_increments` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2233_maximum_product_after_k_increments` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2233_maximum_product_after_k_increments` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2233_maximum_product_after_k_increments` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2233_maximum_product_after_k_increments` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2233_maximum_product_after_k_increments` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2233_maximum_product_after_k_increments` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2233_maximum_product_after_k_increments` |

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
.\scripts\test.ps1 -Folder 2233_maximum_product_after_k_increments -AllLanguages
```

```bash
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --all-languages
```

```zsh
./scripts/test.sh --folder 2233_maximum_product_after_k_increments --all-languages
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
