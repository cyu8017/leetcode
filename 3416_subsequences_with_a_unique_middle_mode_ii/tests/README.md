# Test harness for 3416_subsequences_with_a_unique_middle_mode_ii

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language python
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language javascript
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language typescript
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language java
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language cpp
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language c
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language go
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language rust
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language kotlin
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language swift
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language ruby
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language csharp
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language scala
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language php
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm java java 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm c c 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm go go 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm rust rust 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm swift swift 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm scala scala 3416_subsequences_with_a_unique_middle_mode_ii
docker compose -f docker/docker-compose.yml run --rm php php 3416_subsequences_with_a_unique_middle_mode_ii
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3416_subsequences_with_a_unique_middle_mode_ii` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3416_subsequences_with_a_unique_middle_mode_ii` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3416_subsequences_with_a_unique_middle_mode_ii` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3416_subsequences_with_a_unique_middle_mode_ii` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3416_subsequences_with_a_unique_middle_mode_ii` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3416_subsequences_with_a_unique_middle_mode_ii` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3416_subsequences_with_a_unique_middle_mode_ii` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3416_subsequences_with_a_unique_middle_mode_ii` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3416_subsequences_with_a_unique_middle_mode_ii` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3416_subsequences_with_a_unique_middle_mode_ii` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3416_subsequences_with_a_unique_middle_mode_ii` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3416_subsequences_with_a_unique_middle_mode_ii` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3416_subsequences_with_a_unique_middle_mode_ii` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3416_subsequences_with_a_unique_middle_mode_ii` |

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
.\scripts\test.ps1 -Folder 3416_subsequences_with_a_unique_middle_mode_ii -AllLanguages
```

```bash
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --all-languages
```

```zsh
./scripts/test.sh --folder 3416_subsequences_with_a_unique_middle_mode_ii --all-languages
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
