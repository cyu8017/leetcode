# Test harness for 0814_binary_tree_pruning

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0814_binary_tree_pruning --language python
./scripts/test.sh --folder 0814_binary_tree_pruning --language javascript
./scripts/test.sh --folder 0814_binary_tree_pruning --language typescript
./scripts/test.sh --folder 0814_binary_tree_pruning --language java
./scripts/test.sh --folder 0814_binary_tree_pruning --language cpp
./scripts/test.sh --folder 0814_binary_tree_pruning --language c
./scripts/test.sh --folder 0814_binary_tree_pruning --language go
./scripts/test.sh --folder 0814_binary_tree_pruning --language rust
./scripts/test.sh --folder 0814_binary_tree_pruning --language kotlin
./scripts/test.sh --folder 0814_binary_tree_pruning --language swift
./scripts/test.sh --folder 0814_binary_tree_pruning --language ruby
./scripts/test.sh --folder 0814_binary_tree_pruning --language csharp
./scripts/test.sh --folder 0814_binary_tree_pruning --language scala
./scripts/test.sh --folder 0814_binary_tree_pruning --language php
./scripts/test.sh --folder 0814_binary_tree_pruning --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0814_binary_tree_pruning --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm java java 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm c c 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm go go 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm rust rust 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm swift swift 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm scala scala 0814_binary_tree_pruning
docker compose -f docker/docker-compose.yml run --rm php php 0814_binary_tree_pruning
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0814_binary_tree_pruning` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0814_binary_tree_pruning` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0814_binary_tree_pruning` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0814_binary_tree_pruning` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0814_binary_tree_pruning` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0814_binary_tree_pruning` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0814_binary_tree_pruning` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0814_binary_tree_pruning` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0814_binary_tree_pruning` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0814_binary_tree_pruning` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0814_binary_tree_pruning` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0814_binary_tree_pruning` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0814_binary_tree_pruning` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0814_binary_tree_pruning` |

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
.\scripts\test.ps1 -Folder 0814_binary_tree_pruning -AllLanguages
```

```bash
./scripts/test.sh --folder 0814_binary_tree_pruning --all-languages
```

```zsh
./scripts/test.sh --folder 0814_binary_tree_pruning --all-languages
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
