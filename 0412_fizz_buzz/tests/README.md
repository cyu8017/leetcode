# Test harness for 0412_fizz_buzz

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0412_fizz_buzz -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0412_fizz_buzz --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0412_fizz_buzz --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0412_fizz_buzz --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0412_fizz_buzz --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0412_fizz_buzz --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0412_fizz_buzz --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0412_fizz_buzz --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0412_fizz_buzz --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0412_fizz_buzz --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0412_fizz_buzz --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0412_fizz_buzz --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0412_fizz_buzz --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0412_fizz_buzz --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0412_fizz_buzz --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0412_fizz_buzz --language python
./scripts/test.sh --folder 0412_fizz_buzz --language javascript
./scripts/test.sh --folder 0412_fizz_buzz --language typescript
./scripts/test.sh --folder 0412_fizz_buzz --language java
./scripts/test.sh --folder 0412_fizz_buzz --language cpp
./scripts/test.sh --folder 0412_fizz_buzz --language c
./scripts/test.sh --folder 0412_fizz_buzz --language go
./scripts/test.sh --folder 0412_fizz_buzz --language rust
./scripts/test.sh --folder 0412_fizz_buzz --language kotlin
./scripts/test.sh --folder 0412_fizz_buzz --language swift
./scripts/test.sh --folder 0412_fizz_buzz --language ruby
./scripts/test.sh --folder 0412_fizz_buzz --language csharp
./scripts/test.sh --folder 0412_fizz_buzz --language scala
./scripts/test.sh --folder 0412_fizz_buzz --language php
./scripts/test.sh --folder 0412_fizz_buzz --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0412_fizz_buzz --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0412_fizz_buzz --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0412_fizz_buzz --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0412_fizz_buzz --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0412_fizz_buzz --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0412_fizz_buzz --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0412_fizz_buzz --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0412_fizz_buzz --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0412_fizz_buzz --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0412_fizz_buzz --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0412_fizz_buzz --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0412_fizz_buzz --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0412_fizz_buzz --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0412_fizz_buzz --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm java java 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm c c 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm go go 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm rust rust 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm swift swift 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm scala scala 0412_fizz_buzz
docker compose -f docker/docker-compose.yml run --rm php php 0412_fizz_buzz
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0412_fizz_buzz` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0412_fizz_buzz` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0412_fizz_buzz` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0412_fizz_buzz` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0412_fizz_buzz` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0412_fizz_buzz` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0412_fizz_buzz` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0412_fizz_buzz` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0412_fizz_buzz` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0412_fizz_buzz` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0412_fizz_buzz` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0412_fizz_buzz` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0412_fizz_buzz` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0412_fizz_buzz` |

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
.\scripts\test.ps1 -Folder 0412_fizz_buzz -AllLanguages
```

```bash
./scripts/test.sh --folder 0412_fizz_buzz --all-languages
```

```zsh
./scripts/test.sh --folder 0412_fizz_buzz --all-languages
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
