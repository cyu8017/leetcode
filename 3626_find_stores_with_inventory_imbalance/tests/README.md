# Test harness for 3626_find_stores_with_inventory_imbalance

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language python
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language javascript
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language typescript
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language java
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language cpp
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language c
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language go
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language rust
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language kotlin
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language swift
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language ruby
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language csharp
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language scala
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language php
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm java java 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm c c 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm go go 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm rust rust 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm swift swift 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm scala scala 3626_find_stores_with_inventory_imbalance
docker compose -f docker/docker-compose.yml run --rm php php 3626_find_stores_with_inventory_imbalance
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3626_find_stores_with_inventory_imbalance` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3626_find_stores_with_inventory_imbalance` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3626_find_stores_with_inventory_imbalance` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3626_find_stores_with_inventory_imbalance` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3626_find_stores_with_inventory_imbalance` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3626_find_stores_with_inventory_imbalance` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3626_find_stores_with_inventory_imbalance` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3626_find_stores_with_inventory_imbalance` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3626_find_stores_with_inventory_imbalance` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3626_find_stores_with_inventory_imbalance` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3626_find_stores_with_inventory_imbalance` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3626_find_stores_with_inventory_imbalance` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3626_find_stores_with_inventory_imbalance` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3626_find_stores_with_inventory_imbalance` |

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
.\scripts\test.ps1 -Folder 3626_find_stores_with_inventory_imbalance -AllLanguages
```

```bash
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --all-languages
```

```zsh
./scripts/test.sh --folder 3626_find_stores_with_inventory_imbalance --all-languages
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
