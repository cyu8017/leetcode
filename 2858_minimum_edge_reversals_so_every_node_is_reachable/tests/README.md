# Test harness for 2858_minimum_edge_reversals_so_every_node_is_reachable

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language python
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language javascript
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language typescript
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language java
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language cpp
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language c
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language go
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language rust
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language kotlin
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language swift
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language ruby
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language csharp
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language scala
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language php
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm java java 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm c c 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm go go 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm rust rust 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm swift swift 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm scala scala 2858_minimum_edge_reversals_so_every_node_is_reachable
docker compose -f docker/docker-compose.yml run --rm php php 2858_minimum_edge_reversals_so_every_node_is_reachable
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2858_minimum_edge_reversals_so_every_node_is_reachable` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2858_minimum_edge_reversals_so_every_node_is_reachable` |

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
.\scripts\test.ps1 -Folder 2858_minimum_edge_reversals_so_every_node_is_reachable -AllLanguages
```

```bash
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --all-languages
```

```zsh
./scripts/test.sh --folder 2858_minimum_edge_reversals_so_every_node_is_reachable --all-languages
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
