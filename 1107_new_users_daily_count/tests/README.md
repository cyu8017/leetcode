# Test harness for 1107_new_users_daily_count

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1107_new_users_daily_count -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1107_new_users_daily_count --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1107_new_users_daily_count --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1107_new_users_daily_count --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1107_new_users_daily_count --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1107_new_users_daily_count --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1107_new_users_daily_count --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1107_new_users_daily_count --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1107_new_users_daily_count --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1107_new_users_daily_count --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1107_new_users_daily_count --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1107_new_users_daily_count --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1107_new_users_daily_count --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1107_new_users_daily_count --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1107_new_users_daily_count --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1107_new_users_daily_count --language python
./scripts/test.sh --folder 1107_new_users_daily_count --language javascript
./scripts/test.sh --folder 1107_new_users_daily_count --language typescript
./scripts/test.sh --folder 1107_new_users_daily_count --language java
./scripts/test.sh --folder 1107_new_users_daily_count --language cpp
./scripts/test.sh --folder 1107_new_users_daily_count --language c
./scripts/test.sh --folder 1107_new_users_daily_count --language go
./scripts/test.sh --folder 1107_new_users_daily_count --language rust
./scripts/test.sh --folder 1107_new_users_daily_count --language kotlin
./scripts/test.sh --folder 1107_new_users_daily_count --language swift
./scripts/test.sh --folder 1107_new_users_daily_count --language ruby
./scripts/test.sh --folder 1107_new_users_daily_count --language csharp
./scripts/test.sh --folder 1107_new_users_daily_count --language scala
./scripts/test.sh --folder 1107_new_users_daily_count --language php
./scripts/test.sh --folder 1107_new_users_daily_count --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1107_new_users_daily_count --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1107_new_users_daily_count --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1107_new_users_daily_count --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1107_new_users_daily_count --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1107_new_users_daily_count --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1107_new_users_daily_count --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1107_new_users_daily_count --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1107_new_users_daily_count --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1107_new_users_daily_count --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1107_new_users_daily_count --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1107_new_users_daily_count --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1107_new_users_daily_count --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1107_new_users_daily_count --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1107_new_users_daily_count --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm java java 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm c c 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm go go 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm rust rust 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm swift swift 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm scala scala 1107_new_users_daily_count
docker compose -f docker/docker-compose.yml run --rm php php 1107_new_users_daily_count
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1107_new_users_daily_count` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1107_new_users_daily_count` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1107_new_users_daily_count` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1107_new_users_daily_count` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1107_new_users_daily_count` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1107_new_users_daily_count` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1107_new_users_daily_count` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1107_new_users_daily_count` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1107_new_users_daily_count` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1107_new_users_daily_count` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1107_new_users_daily_count` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1107_new_users_daily_count` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1107_new_users_daily_count` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1107_new_users_daily_count` |

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
.\scripts\test.ps1 -Folder 1107_new_users_daily_count -AllLanguages
```

```bash
./scripts/test.sh --folder 1107_new_users_daily_count --all-languages
```

```zsh
./scripts/test.sh --folder 1107_new_users_daily_count --all-languages
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
