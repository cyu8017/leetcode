# Test harness for 0483_smallest_good_base

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0483_smallest_good_base -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0483_smallest_good_base --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0483_smallest_good_base --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0483_smallest_good_base --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0483_smallest_good_base --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0483_smallest_good_base --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0483_smallest_good_base --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0483_smallest_good_base --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0483_smallest_good_base --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0483_smallest_good_base --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0483_smallest_good_base --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0483_smallest_good_base --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0483_smallest_good_base --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0483_smallest_good_base --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0483_smallest_good_base --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0483_smallest_good_base --language python
./scripts/test.sh --folder 0483_smallest_good_base --language javascript
./scripts/test.sh --folder 0483_smallest_good_base --language typescript
./scripts/test.sh --folder 0483_smallest_good_base --language java
./scripts/test.sh --folder 0483_smallest_good_base --language cpp
./scripts/test.sh --folder 0483_smallest_good_base --language c
./scripts/test.sh --folder 0483_smallest_good_base --language go
./scripts/test.sh --folder 0483_smallest_good_base --language rust
./scripts/test.sh --folder 0483_smallest_good_base --language kotlin
./scripts/test.sh --folder 0483_smallest_good_base --language swift
./scripts/test.sh --folder 0483_smallest_good_base --language ruby
./scripts/test.sh --folder 0483_smallest_good_base --language csharp
./scripts/test.sh --folder 0483_smallest_good_base --language scala
./scripts/test.sh --folder 0483_smallest_good_base --language php
./scripts/test.sh --folder 0483_smallest_good_base --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0483_smallest_good_base --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0483_smallest_good_base --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0483_smallest_good_base --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0483_smallest_good_base --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0483_smallest_good_base --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0483_smallest_good_base --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0483_smallest_good_base --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0483_smallest_good_base --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0483_smallest_good_base --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0483_smallest_good_base --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0483_smallest_good_base --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0483_smallest_good_base --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0483_smallest_good_base --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0483_smallest_good_base --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm java java 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm c c 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm go go 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm rust rust 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm swift swift 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm scala scala 0483_smallest_good_base
docker compose -f docker/docker-compose.yml run --rm php php 0483_smallest_good_base
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0483_smallest_good_base` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0483_smallest_good_base` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0483_smallest_good_base` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0483_smallest_good_base` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0483_smallest_good_base` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0483_smallest_good_base` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0483_smallest_good_base` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0483_smallest_good_base` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0483_smallest_good_base` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0483_smallest_good_base` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0483_smallest_good_base` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0483_smallest_good_base` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0483_smallest_good_base` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0483_smallest_good_base` |

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
.\scripts\test.ps1 -Folder 0483_smallest_good_base -AllLanguages
```

```bash
./scripts/test.sh --folder 0483_smallest_good_base --all-languages
```

```zsh
./scripts/test.sh --folder 0483_smallest_good_base --all-languages
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
