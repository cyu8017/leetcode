# Test harness for 0919_complete_binary_tree_inserter

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language python
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language javascript
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language typescript
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language java
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language cpp
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language c
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language go
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language rust
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language kotlin
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language swift
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language ruby
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language csharp
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language scala
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language php
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0919_complete_binary_tree_inserter --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm java java 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm c c 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm go go 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm rust rust 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm swift swift 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm scala scala 0919_complete_binary_tree_inserter
docker compose -f docker/docker-compose.yml run --rm php php 0919_complete_binary_tree_inserter
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0919_complete_binary_tree_inserter` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0919_complete_binary_tree_inserter` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0919_complete_binary_tree_inserter` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0919_complete_binary_tree_inserter` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0919_complete_binary_tree_inserter` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0919_complete_binary_tree_inserter` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0919_complete_binary_tree_inserter` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0919_complete_binary_tree_inserter` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0919_complete_binary_tree_inserter` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0919_complete_binary_tree_inserter` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0919_complete_binary_tree_inserter` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0919_complete_binary_tree_inserter` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0919_complete_binary_tree_inserter` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0919_complete_binary_tree_inserter` |

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
.\scripts\test.ps1 -Folder 0919_complete_binary_tree_inserter -AllLanguages
```

```bash
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --all-languages
```

```zsh
./scripts/test.sh --folder 0919_complete_binary_tree_inserter --all-languages
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
