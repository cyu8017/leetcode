# Test harness for 2368_reachable_nodes_with_restrictions

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language python
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language javascript
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language typescript
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language java
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language cpp
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language c
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language go
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language rust
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language kotlin
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language swift
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language ruby
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language csharp
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language scala
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language php
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm java java 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm c c 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm go go 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm rust rust 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm swift swift 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm scala scala 2368_reachable_nodes_with_restrictions
docker compose -f docker/docker-compose.yml run --rm php php 2368_reachable_nodes_with_restrictions
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2368_reachable_nodes_with_restrictions` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2368_reachable_nodes_with_restrictions` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2368_reachable_nodes_with_restrictions` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2368_reachable_nodes_with_restrictions` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2368_reachable_nodes_with_restrictions` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2368_reachable_nodes_with_restrictions` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2368_reachable_nodes_with_restrictions` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2368_reachable_nodes_with_restrictions` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2368_reachable_nodes_with_restrictions` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2368_reachable_nodes_with_restrictions` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2368_reachable_nodes_with_restrictions` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2368_reachable_nodes_with_restrictions` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2368_reachable_nodes_with_restrictions` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2368_reachable_nodes_with_restrictions` |

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
.\scripts\test.ps1 -Folder 2368_reachable_nodes_with_restrictions -AllLanguages
```

```bash
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --all-languages
```

```zsh
./scripts/test.sh --folder 2368_reachable_nodes_with_restrictions --all-languages
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
