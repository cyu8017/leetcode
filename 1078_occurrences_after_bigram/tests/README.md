# Test harness for 1078_occurrences_after_bigram

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1078_occurrences_after_bigram --language python
./scripts/test.sh --folder 1078_occurrences_after_bigram --language javascript
./scripts/test.sh --folder 1078_occurrences_after_bigram --language typescript
./scripts/test.sh --folder 1078_occurrences_after_bigram --language java
./scripts/test.sh --folder 1078_occurrences_after_bigram --language cpp
./scripts/test.sh --folder 1078_occurrences_after_bigram --language c
./scripts/test.sh --folder 1078_occurrences_after_bigram --language go
./scripts/test.sh --folder 1078_occurrences_after_bigram --language rust
./scripts/test.sh --folder 1078_occurrences_after_bigram --language kotlin
./scripts/test.sh --folder 1078_occurrences_after_bigram --language swift
./scripts/test.sh --folder 1078_occurrences_after_bigram --language ruby
./scripts/test.sh --folder 1078_occurrences_after_bigram --language csharp
./scripts/test.sh --folder 1078_occurrences_after_bigram --language scala
./scripts/test.sh --folder 1078_occurrences_after_bigram --language php
./scripts/test.sh --folder 1078_occurrences_after_bigram --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1078_occurrences_after_bigram --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm java java 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm c c 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm go go 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm rust rust 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm swift swift 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm scala scala 1078_occurrences_after_bigram
docker compose -f docker/docker-compose.yml run --rm php php 1078_occurrences_after_bigram
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1078_occurrences_after_bigram` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1078_occurrences_after_bigram` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1078_occurrences_after_bigram` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1078_occurrences_after_bigram` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1078_occurrences_after_bigram` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1078_occurrences_after_bigram` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1078_occurrences_after_bigram` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1078_occurrences_after_bigram` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1078_occurrences_after_bigram` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1078_occurrences_after_bigram` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1078_occurrences_after_bigram` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1078_occurrences_after_bigram` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1078_occurrences_after_bigram` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1078_occurrences_after_bigram` |

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
.\scripts\test.ps1 -Folder 1078_occurrences_after_bigram -AllLanguages
```

```bash
./scripts/test.sh --folder 1078_occurrences_after_bigram --all-languages
```

```zsh
./scripts/test.sh --folder 1078_occurrences_after_bigram --all-languages
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
