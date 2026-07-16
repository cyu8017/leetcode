# Test harness for 1454_active_users

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1454_active_users -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1454_active_users -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1454_active_users -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1454_active_users -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1454_active_users -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1454_active_users -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1454_active_users -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1454_active_users -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1454_active_users -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1454_active_users -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1454_active_users -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1454_active_users -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1454_active_users -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1454_active_users -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1454_active_users --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1454_active_users --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1454_active_users --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1454_active_users --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1454_active_users --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1454_active_users --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1454_active_users --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1454_active_users --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1454_active_users --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1454_active_users --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1454_active_users --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1454_active_users --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1454_active_users --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1454_active_users --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1454_active_users --language python
./scripts/test.sh --folder 1454_active_users --language javascript
./scripts/test.sh --folder 1454_active_users --language typescript
./scripts/test.sh --folder 1454_active_users --language java
./scripts/test.sh --folder 1454_active_users --language cpp
./scripts/test.sh --folder 1454_active_users --language c
./scripts/test.sh --folder 1454_active_users --language go
./scripts/test.sh --folder 1454_active_users --language rust
./scripts/test.sh --folder 1454_active_users --language kotlin
./scripts/test.sh --folder 1454_active_users --language swift
./scripts/test.sh --folder 1454_active_users --language ruby
./scripts/test.sh --folder 1454_active_users --language csharp
./scripts/test.sh --folder 1454_active_users --language scala
./scripts/test.sh --folder 1454_active_users --language php
./scripts/test.sh --folder 1454_active_users --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1454_active_users --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1454_active_users --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1454_active_users --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1454_active_users --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1454_active_users --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1454_active_users --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1454_active_users --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1454_active_users --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1454_active_users --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1454_active_users --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1454_active_users --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1454_active_users --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1454_active_users --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1454_active_users --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1454_active_users
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1454_active_users
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1454_active_users
docker compose -f docker/docker-compose.yml run --rm java java 1454_active_users
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1454_active_users
docker compose -f docker/docker-compose.yml run --rm c c 1454_active_users
docker compose -f docker/docker-compose.yml run --rm go go 1454_active_users
docker compose -f docker/docker-compose.yml run --rm rust rust 1454_active_users
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1454_active_users
docker compose -f docker/docker-compose.yml run --rm swift swift 1454_active_users
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1454_active_users
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1454_active_users
docker compose -f docker/docker-compose.yml run --rm scala scala 1454_active_users
docker compose -f docker/docker-compose.yml run --rm php php 1454_active_users
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1454_active_users` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1454_active_users` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1454_active_users` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1454_active_users` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1454_active_users` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1454_active_users` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1454_active_users` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1454_active_users` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1454_active_users` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1454_active_users` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1454_active_users` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1454_active_users` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1454_active_users` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1454_active_users` |

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
.\scripts\test.ps1 -Folder 1454_active_users -AllLanguages
```

```bash
./scripts/test.sh --folder 1454_active_users --all-languages
```

```zsh
./scripts/test.sh --folder 1454_active_users --all-languages
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
