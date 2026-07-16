# Test harness for 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language python
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language javascript
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language typescript
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language java
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language cpp
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language c
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language go
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language rust
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language kotlin
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language swift
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language ruby
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language csharp
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language scala
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language php
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm java java 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm c c 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm go go 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm rust rust 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm swift swift 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm scala scala 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
docker compose -f docker/docker-compose.yml run --rm php php 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable` |

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
.\scripts\test.ps1 -Folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable -AllLanguages
```

```bash
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --all-languages
```

```zsh
./scripts/test.sh --folder 1579_remove_max_number_of_edges_to_keep_graph_fully_traversable --all-languages
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
