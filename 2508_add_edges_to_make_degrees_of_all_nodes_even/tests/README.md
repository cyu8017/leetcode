# Test harness for 2508_add_edges_to_make_degrees_of_all_nodes_even

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language python
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language javascript
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language typescript
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language java
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language cpp
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language c
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language go
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language rust
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language kotlin
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language swift
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language ruby
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language csharp
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language scala
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language php
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm java java 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm c c 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm go go 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm rust rust 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm swift swift 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm scala scala 2508_add_edges_to_make_degrees_of_all_nodes_even
docker compose -f docker/docker-compose.yml run --rm php php 2508_add_edges_to_make_degrees_of_all_nodes_even
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2508_add_edges_to_make_degrees_of_all_nodes_even` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2508_add_edges_to_make_degrees_of_all_nodes_even` |

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
.\scripts\test.ps1 -Folder 2508_add_edges_to_make_degrees_of_all_nodes_even -AllLanguages
```

```bash
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --all-languages
```

```zsh
./scripts/test.sh --folder 2508_add_edges_to_make_degrees_of_all_nodes_even --all-languages
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
