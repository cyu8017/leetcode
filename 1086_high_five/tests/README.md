# Test harness for 1086_high_five

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1086_high_five -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1086_high_five -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1086_high_five -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1086_high_five -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1086_high_five -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1086_high_five -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1086_high_five -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1086_high_five -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1086_high_five -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1086_high_five -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1086_high_five -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1086_high_five -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1086_high_five -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1086_high_five -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1086_high_five --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1086_high_five --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1086_high_five --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1086_high_five --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1086_high_five --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1086_high_five --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1086_high_five --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1086_high_five --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1086_high_five --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1086_high_five --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1086_high_five --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1086_high_five --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1086_high_five --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1086_high_five --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1086_high_five --language python
./scripts/test.sh --folder 1086_high_five --language javascript
./scripts/test.sh --folder 1086_high_five --language typescript
./scripts/test.sh --folder 1086_high_five --language java
./scripts/test.sh --folder 1086_high_five --language cpp
./scripts/test.sh --folder 1086_high_five --language c
./scripts/test.sh --folder 1086_high_five --language go
./scripts/test.sh --folder 1086_high_five --language rust
./scripts/test.sh --folder 1086_high_five --language kotlin
./scripts/test.sh --folder 1086_high_five --language swift
./scripts/test.sh --folder 1086_high_five --language ruby
./scripts/test.sh --folder 1086_high_five --language csharp
./scripts/test.sh --folder 1086_high_five --language scala
./scripts/test.sh --folder 1086_high_five --language php
./scripts/test.sh --folder 1086_high_five --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1086_high_five --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1086_high_five --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1086_high_five --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1086_high_five --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1086_high_five --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1086_high_five --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1086_high_five --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1086_high_five --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1086_high_five --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1086_high_five --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1086_high_five --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1086_high_five --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1086_high_five --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1086_high_five --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1086_high_five
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1086_high_five
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1086_high_five
docker compose -f docker/docker-compose.yml run --rm java java 1086_high_five
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1086_high_five
docker compose -f docker/docker-compose.yml run --rm c c 1086_high_five
docker compose -f docker/docker-compose.yml run --rm go go 1086_high_five
docker compose -f docker/docker-compose.yml run --rm rust rust 1086_high_five
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1086_high_five
docker compose -f docker/docker-compose.yml run --rm swift swift 1086_high_five
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1086_high_five
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1086_high_five
docker compose -f docker/docker-compose.yml run --rm scala scala 1086_high_five
docker compose -f docker/docker-compose.yml run --rm php php 1086_high_five
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1086_high_five` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1086_high_five` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1086_high_five` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1086_high_five` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1086_high_five` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1086_high_five` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1086_high_five` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1086_high_five` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1086_high_five` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1086_high_five` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1086_high_five` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1086_high_five` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1086_high_five` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1086_high_five` |

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
.\scripts\test.ps1 -Folder 1086_high_five -AllLanguages
```

```bash
./scripts/test.sh --folder 1086_high_five --all-languages
```

```zsh
./scripts/test.sh --folder 1086_high_five --all-languages
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
