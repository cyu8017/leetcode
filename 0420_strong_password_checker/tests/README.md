# Test harness for 0420_strong_password_checker

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0420_strong_password_checker -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0420_strong_password_checker --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0420_strong_password_checker --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0420_strong_password_checker --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0420_strong_password_checker --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0420_strong_password_checker --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0420_strong_password_checker --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0420_strong_password_checker --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0420_strong_password_checker --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0420_strong_password_checker --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0420_strong_password_checker --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0420_strong_password_checker --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0420_strong_password_checker --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0420_strong_password_checker --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0420_strong_password_checker --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0420_strong_password_checker --language python
./scripts/test.sh --folder 0420_strong_password_checker --language javascript
./scripts/test.sh --folder 0420_strong_password_checker --language typescript
./scripts/test.sh --folder 0420_strong_password_checker --language java
./scripts/test.sh --folder 0420_strong_password_checker --language cpp
./scripts/test.sh --folder 0420_strong_password_checker --language c
./scripts/test.sh --folder 0420_strong_password_checker --language go
./scripts/test.sh --folder 0420_strong_password_checker --language rust
./scripts/test.sh --folder 0420_strong_password_checker --language kotlin
./scripts/test.sh --folder 0420_strong_password_checker --language swift
./scripts/test.sh --folder 0420_strong_password_checker --language ruby
./scripts/test.sh --folder 0420_strong_password_checker --language csharp
./scripts/test.sh --folder 0420_strong_password_checker --language scala
./scripts/test.sh --folder 0420_strong_password_checker --language php
./scripts/test.sh --folder 0420_strong_password_checker --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0420_strong_password_checker --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0420_strong_password_checker --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0420_strong_password_checker --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0420_strong_password_checker --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0420_strong_password_checker --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0420_strong_password_checker --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0420_strong_password_checker --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0420_strong_password_checker --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0420_strong_password_checker --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0420_strong_password_checker --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0420_strong_password_checker --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0420_strong_password_checker --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0420_strong_password_checker --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0420_strong_password_checker --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm java java 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm c c 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm go go 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm rust rust 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm swift swift 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm scala scala 0420_strong_password_checker
docker compose -f docker/docker-compose.yml run --rm php php 0420_strong_password_checker
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0420_strong_password_checker` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0420_strong_password_checker` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0420_strong_password_checker` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0420_strong_password_checker` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0420_strong_password_checker` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0420_strong_password_checker` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0420_strong_password_checker` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0420_strong_password_checker` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0420_strong_password_checker` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0420_strong_password_checker` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0420_strong_password_checker` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0420_strong_password_checker` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0420_strong_password_checker` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0420_strong_password_checker` |

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
.\scripts\test.ps1 -Folder 0420_strong_password_checker -AllLanguages
```

```bash
./scripts/test.sh --folder 0420_strong_password_checker --all-languages
```

```zsh
./scripts/test.sh --folder 0420_strong_password_checker --all-languages
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
