# Test harness for 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language python
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language javascript
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language typescript
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language java
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language cpp
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language c
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language go
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language rust
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language kotlin
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language swift
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language ruby
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language csharp
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language scala
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language php
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm java java 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm c c 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm go go 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm rust rust 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm swift swift 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm scala scala 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
docker compose -f docker/docker-compose.yml run --rm php php 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network` |

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
.\scripts\test.ps1 -Folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network -AllLanguages
```

```bash
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --all-languages
```

```zsh
./scripts/test.sh --folder 3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network --all-languages
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
