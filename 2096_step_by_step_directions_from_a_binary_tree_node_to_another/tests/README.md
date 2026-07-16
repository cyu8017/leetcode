# Test harness for 2096_step_by_step_directions_from_a_binary_tree_node_to_another

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language python
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language javascript
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language typescript
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language java
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language cpp
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language c
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language go
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language rust
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language kotlin
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language swift
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language ruby
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language csharp
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language scala
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language php
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm java java 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm c c 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm go go 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm rust rust 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm swift swift 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm scala scala 2096_step_by_step_directions_from_a_binary_tree_node_to_another
docker compose -f docker/docker-compose.yml run --rm php php 2096_step_by_step_directions_from_a_binary_tree_node_to_another
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2096_step_by_step_directions_from_a_binary_tree_node_to_another` |

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
.\scripts\test.ps1 -Folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another -AllLanguages
```

```bash
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --all-languages
```

```zsh
./scripts/test.sh --folder 2096_step_by_step_directions_from_a_binary_tree_node_to_another --all-languages
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
