# Test harness for 0802_find_eventual_safe_states

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0802_find_eventual_safe_states --language python
./scripts/test.sh --folder 0802_find_eventual_safe_states --language javascript
./scripts/test.sh --folder 0802_find_eventual_safe_states --language typescript
./scripts/test.sh --folder 0802_find_eventual_safe_states --language java
./scripts/test.sh --folder 0802_find_eventual_safe_states --language cpp
./scripts/test.sh --folder 0802_find_eventual_safe_states --language c
./scripts/test.sh --folder 0802_find_eventual_safe_states --language go
./scripts/test.sh --folder 0802_find_eventual_safe_states --language rust
./scripts/test.sh --folder 0802_find_eventual_safe_states --language kotlin
./scripts/test.sh --folder 0802_find_eventual_safe_states --language swift
./scripts/test.sh --folder 0802_find_eventual_safe_states --language ruby
./scripts/test.sh --folder 0802_find_eventual_safe_states --language csharp
./scripts/test.sh --folder 0802_find_eventual_safe_states --language scala
./scripts/test.sh --folder 0802_find_eventual_safe_states --language php
./scripts/test.sh --folder 0802_find_eventual_safe_states --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0802_find_eventual_safe_states --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm java java 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm c c 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm go go 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm rust rust 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm swift swift 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm scala scala 0802_find_eventual_safe_states
docker compose -f docker/docker-compose.yml run --rm php php 0802_find_eventual_safe_states
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0802_find_eventual_safe_states` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0802_find_eventual_safe_states` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0802_find_eventual_safe_states` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0802_find_eventual_safe_states` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0802_find_eventual_safe_states` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0802_find_eventual_safe_states` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0802_find_eventual_safe_states` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0802_find_eventual_safe_states` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0802_find_eventual_safe_states` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0802_find_eventual_safe_states` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0802_find_eventual_safe_states` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0802_find_eventual_safe_states` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0802_find_eventual_safe_states` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0802_find_eventual_safe_states` |

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
.\scripts\test.ps1 -Folder 0802_find_eventual_safe_states -AllLanguages
```

```bash
./scripts/test.sh --folder 0802_find_eventual_safe_states --all-languages
```

```zsh
./scripts/test.sh --folder 0802_find_eventual_safe_states --all-languages
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
