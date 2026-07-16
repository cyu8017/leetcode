# Test harness for 3089_find_bursty_behavior

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3089_find_bursty_behavior --language python
./scripts/test.sh --folder 3089_find_bursty_behavior --language javascript
./scripts/test.sh --folder 3089_find_bursty_behavior --language typescript
./scripts/test.sh --folder 3089_find_bursty_behavior --language java
./scripts/test.sh --folder 3089_find_bursty_behavior --language cpp
./scripts/test.sh --folder 3089_find_bursty_behavior --language c
./scripts/test.sh --folder 3089_find_bursty_behavior --language go
./scripts/test.sh --folder 3089_find_bursty_behavior --language rust
./scripts/test.sh --folder 3089_find_bursty_behavior --language kotlin
./scripts/test.sh --folder 3089_find_bursty_behavior --language swift
./scripts/test.sh --folder 3089_find_bursty_behavior --language ruby
./scripts/test.sh --folder 3089_find_bursty_behavior --language csharp
./scripts/test.sh --folder 3089_find_bursty_behavior --language scala
./scripts/test.sh --folder 3089_find_bursty_behavior --language php
./scripts/test.sh --folder 3089_find_bursty_behavior --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3089_find_bursty_behavior --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm java java 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm c c 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm go go 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm rust rust 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm swift swift 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm scala scala 3089_find_bursty_behavior
docker compose -f docker/docker-compose.yml run --rm php php 3089_find_bursty_behavior
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3089_find_bursty_behavior` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3089_find_bursty_behavior` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3089_find_bursty_behavior` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3089_find_bursty_behavior` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3089_find_bursty_behavior` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3089_find_bursty_behavior` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3089_find_bursty_behavior` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3089_find_bursty_behavior` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3089_find_bursty_behavior` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3089_find_bursty_behavior` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3089_find_bursty_behavior` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3089_find_bursty_behavior` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3089_find_bursty_behavior` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3089_find_bursty_behavior` |

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
.\scripts\test.ps1 -Folder 3089_find_bursty_behavior -AllLanguages
```

```bash
./scripts/test.sh --folder 3089_find_bursty_behavior --all-languages
```

```zsh
./scripts/test.sh --folder 3089_find_bursty_behavior --all-languages
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
