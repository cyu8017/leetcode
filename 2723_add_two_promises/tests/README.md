# Test harness for 2723_add_two_promises

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2723_add_two_promises -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2723_add_two_promises --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2723_add_two_promises --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2723_add_two_promises --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2723_add_two_promises --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2723_add_two_promises --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2723_add_two_promises --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2723_add_two_promises --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2723_add_two_promises --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2723_add_two_promises --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2723_add_two_promises --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2723_add_two_promises --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2723_add_two_promises --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2723_add_two_promises --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2723_add_two_promises --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2723_add_two_promises --language python
./scripts/test.sh --folder 2723_add_two_promises --language javascript
./scripts/test.sh --folder 2723_add_two_promises --language typescript
./scripts/test.sh --folder 2723_add_two_promises --language java
./scripts/test.sh --folder 2723_add_two_promises --language cpp
./scripts/test.sh --folder 2723_add_two_promises --language c
./scripts/test.sh --folder 2723_add_two_promises --language go
./scripts/test.sh --folder 2723_add_two_promises --language rust
./scripts/test.sh --folder 2723_add_two_promises --language kotlin
./scripts/test.sh --folder 2723_add_two_promises --language swift
./scripts/test.sh --folder 2723_add_two_promises --language ruby
./scripts/test.sh --folder 2723_add_two_promises --language csharp
./scripts/test.sh --folder 2723_add_two_promises --language scala
./scripts/test.sh --folder 2723_add_two_promises --language php
./scripts/test.sh --folder 2723_add_two_promises --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2723_add_two_promises --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2723_add_two_promises --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2723_add_two_promises --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2723_add_two_promises --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2723_add_two_promises --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2723_add_two_promises --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2723_add_two_promises --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2723_add_two_promises --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2723_add_two_promises --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2723_add_two_promises --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2723_add_two_promises --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2723_add_two_promises --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2723_add_two_promises --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2723_add_two_promises --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm java java 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm c c 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm go go 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm rust rust 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm swift swift 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm scala scala 2723_add_two_promises
docker compose -f docker/docker-compose.yml run --rm php php 2723_add_two_promises
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2723_add_two_promises` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2723_add_two_promises` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2723_add_two_promises` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2723_add_two_promises` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2723_add_two_promises` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2723_add_two_promises` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2723_add_two_promises` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2723_add_two_promises` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2723_add_two_promises` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2723_add_two_promises` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2723_add_two_promises` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2723_add_two_promises` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2723_add_two_promises` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2723_add_two_promises` |

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
.\scripts\test.ps1 -Folder 2723_add_two_promises -AllLanguages
```

```bash
./scripts/test.sh --folder 2723_add_two_promises --all-languages
```

```zsh
./scripts/test.sh --folder 2723_add_two_promises --all-languages
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
