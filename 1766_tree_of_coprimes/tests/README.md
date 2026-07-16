# Test harness for 1766_tree_of_coprimes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1766_tree_of_coprimes --language python
./scripts/test.sh --folder 1766_tree_of_coprimes --language javascript
./scripts/test.sh --folder 1766_tree_of_coprimes --language typescript
./scripts/test.sh --folder 1766_tree_of_coprimes --language java
./scripts/test.sh --folder 1766_tree_of_coprimes --language cpp
./scripts/test.sh --folder 1766_tree_of_coprimes --language c
./scripts/test.sh --folder 1766_tree_of_coprimes --language go
./scripts/test.sh --folder 1766_tree_of_coprimes --language rust
./scripts/test.sh --folder 1766_tree_of_coprimes --language kotlin
./scripts/test.sh --folder 1766_tree_of_coprimes --language swift
./scripts/test.sh --folder 1766_tree_of_coprimes --language ruby
./scripts/test.sh --folder 1766_tree_of_coprimes --language csharp
./scripts/test.sh --folder 1766_tree_of_coprimes --language scala
./scripts/test.sh --folder 1766_tree_of_coprimes --language php
./scripts/test.sh --folder 1766_tree_of_coprimes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1766_tree_of_coprimes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm java java 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm c c 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm go go 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm rust rust 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm swift swift 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm scala scala 1766_tree_of_coprimes
docker compose -f docker/docker-compose.yml run --rm php php 1766_tree_of_coprimes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1766_tree_of_coprimes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1766_tree_of_coprimes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1766_tree_of_coprimes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1766_tree_of_coprimes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1766_tree_of_coprimes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1766_tree_of_coprimes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1766_tree_of_coprimes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1766_tree_of_coprimes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1766_tree_of_coprimes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1766_tree_of_coprimes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1766_tree_of_coprimes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1766_tree_of_coprimes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1766_tree_of_coprimes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1766_tree_of_coprimes` |

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
.\scripts\test.ps1 -Folder 1766_tree_of_coprimes -AllLanguages
```

```bash
./scripts/test.sh --folder 1766_tree_of_coprimes --all-languages
```

```zsh
./scripts/test.sh --folder 1766_tree_of_coprimes --all-languages
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
