# Test harness for 3793_find_users_with_high_token_usage

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language python
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language javascript
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language typescript
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language java
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language cpp
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language c
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language go
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language rust
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language kotlin
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language swift
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language ruby
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language csharp
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language scala
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language php
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3793_find_users_with_high_token_usage --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm java java 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm c c 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm go go 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm rust rust 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm swift swift 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm scala scala 3793_find_users_with_high_token_usage
docker compose -f docker/docker-compose.yml run --rm php php 3793_find_users_with_high_token_usage
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3793_find_users_with_high_token_usage` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3793_find_users_with_high_token_usage` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3793_find_users_with_high_token_usage` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3793_find_users_with_high_token_usage` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3793_find_users_with_high_token_usage` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3793_find_users_with_high_token_usage` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3793_find_users_with_high_token_usage` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3793_find_users_with_high_token_usage` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3793_find_users_with_high_token_usage` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3793_find_users_with_high_token_usage` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3793_find_users_with_high_token_usage` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3793_find_users_with_high_token_usage` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3793_find_users_with_high_token_usage` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3793_find_users_with_high_token_usage` |

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
.\scripts\test.ps1 -Folder 3793_find_users_with_high_token_usage -AllLanguages
```

```bash
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --all-languages
```

```zsh
./scripts/test.sh --folder 3793_find_users_with_high_token_usage --all-languages
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
