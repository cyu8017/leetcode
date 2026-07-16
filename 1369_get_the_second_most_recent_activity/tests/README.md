# Test harness for 1369_get_the_second_most_recent_activity

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language python
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language javascript
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language typescript
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language java
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language cpp
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language c
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language go
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language rust
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language kotlin
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language swift
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language ruby
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language csharp
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language scala
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language php
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm java java 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm c c 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm go go 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm rust rust 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm swift swift 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm scala scala 1369_get_the_second_most_recent_activity
docker compose -f docker/docker-compose.yml run --rm php php 1369_get_the_second_most_recent_activity
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1369_get_the_second_most_recent_activity` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1369_get_the_second_most_recent_activity` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1369_get_the_second_most_recent_activity` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1369_get_the_second_most_recent_activity` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1369_get_the_second_most_recent_activity` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1369_get_the_second_most_recent_activity` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1369_get_the_second_most_recent_activity` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1369_get_the_second_most_recent_activity` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1369_get_the_second_most_recent_activity` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1369_get_the_second_most_recent_activity` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1369_get_the_second_most_recent_activity` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1369_get_the_second_most_recent_activity` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1369_get_the_second_most_recent_activity` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1369_get_the_second_most_recent_activity` |

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
.\scripts\test.ps1 -Folder 1369_get_the_second_most_recent_activity -AllLanguages
```

```bash
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --all-languages
```

```zsh
./scripts/test.sh --folder 1369_get_the_second_most_recent_activity --all-languages
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
