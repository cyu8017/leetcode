# Test harness for 0343_integer_break

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0343_integer_break -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0343_integer_break --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0343_integer_break --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0343_integer_break --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0343_integer_break --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0343_integer_break --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0343_integer_break --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0343_integer_break --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0343_integer_break --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0343_integer_break --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0343_integer_break --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0343_integer_break --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0343_integer_break --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0343_integer_break --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0343_integer_break --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0343_integer_break --language python
./scripts/test.sh --folder 0343_integer_break --language javascript
./scripts/test.sh --folder 0343_integer_break --language typescript
./scripts/test.sh --folder 0343_integer_break --language java
./scripts/test.sh --folder 0343_integer_break --language cpp
./scripts/test.sh --folder 0343_integer_break --language c
./scripts/test.sh --folder 0343_integer_break --language go
./scripts/test.sh --folder 0343_integer_break --language rust
./scripts/test.sh --folder 0343_integer_break --language kotlin
./scripts/test.sh --folder 0343_integer_break --language swift
./scripts/test.sh --folder 0343_integer_break --language ruby
./scripts/test.sh --folder 0343_integer_break --language csharp
./scripts/test.sh --folder 0343_integer_break --language scala
./scripts/test.sh --folder 0343_integer_break --language php
./scripts/test.sh --folder 0343_integer_break --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0343_integer_break --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0343_integer_break --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0343_integer_break --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0343_integer_break --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0343_integer_break --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0343_integer_break --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0343_integer_break --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0343_integer_break --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0343_integer_break --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0343_integer_break --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0343_integer_break --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0343_integer_break --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0343_integer_break --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0343_integer_break --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm java java 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm c c 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm go go 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm rust rust 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm swift swift 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm scala scala 0343_integer_break
docker compose -f docker/docker-compose.yml run --rm php php 0343_integer_break
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0343_integer_break` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0343_integer_break` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0343_integer_break` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0343_integer_break` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0343_integer_break` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0343_integer_break` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0343_integer_break` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0343_integer_break` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0343_integer_break` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0343_integer_break` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0343_integer_break` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0343_integer_break` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0343_integer_break` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0343_integer_break` |

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
.\scripts\test.ps1 -Folder 0343_integer_break -AllLanguages
```

```bash
./scripts/test.sh --folder 0343_integer_break --all-languages
```

```zsh
./scripts/test.sh --folder 0343_integer_break --all-languages
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
