# Test harness for 3789_minimum_cost_to_acquire_required_items

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language python
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language javascript
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language typescript
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language java
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language cpp
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language c
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language go
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language rust
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language kotlin
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language swift
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language ruby
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language csharp
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language scala
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language php
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm java java 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm c c 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm go go 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm rust rust 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm swift swift 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm scala scala 3789_minimum_cost_to_acquire_required_items
docker compose -f docker/docker-compose.yml run --rm php php 3789_minimum_cost_to_acquire_required_items
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3789_minimum_cost_to_acquire_required_items` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3789_minimum_cost_to_acquire_required_items` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3789_minimum_cost_to_acquire_required_items` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3789_minimum_cost_to_acquire_required_items` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3789_minimum_cost_to_acquire_required_items` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3789_minimum_cost_to_acquire_required_items` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3789_minimum_cost_to_acquire_required_items` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3789_minimum_cost_to_acquire_required_items` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3789_minimum_cost_to_acquire_required_items` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3789_minimum_cost_to_acquire_required_items` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3789_minimum_cost_to_acquire_required_items` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3789_minimum_cost_to_acquire_required_items` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3789_minimum_cost_to_acquire_required_items` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3789_minimum_cost_to_acquire_required_items` |

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
.\scripts\test.ps1 -Folder 3789_minimum_cost_to_acquire_required_items -AllLanguages
```

```bash
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --all-languages
```

```zsh
./scripts/test.sh --folder 3789_minimum_cost_to_acquire_required_items --all-languages
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
