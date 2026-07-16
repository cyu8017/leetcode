# Test harness for 1936_add_minimum_number_of_rungs

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language python
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language javascript
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language typescript
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language java
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language cpp
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language c
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language go
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language rust
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language kotlin
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language swift
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language ruby
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language csharp
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language scala
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language php
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm java java 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm c c 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm go go 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm rust rust 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm swift swift 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm scala scala 1936_add_minimum_number_of_rungs
docker compose -f docker/docker-compose.yml run --rm php php 1936_add_minimum_number_of_rungs
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1936_add_minimum_number_of_rungs` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1936_add_minimum_number_of_rungs` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1936_add_minimum_number_of_rungs` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1936_add_minimum_number_of_rungs` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1936_add_minimum_number_of_rungs` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1936_add_minimum_number_of_rungs` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1936_add_minimum_number_of_rungs` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1936_add_minimum_number_of_rungs` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1936_add_minimum_number_of_rungs` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1936_add_minimum_number_of_rungs` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1936_add_minimum_number_of_rungs` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1936_add_minimum_number_of_rungs` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1936_add_minimum_number_of_rungs` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1936_add_minimum_number_of_rungs` |

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
.\scripts\test.ps1 -Folder 1936_add_minimum_number_of_rungs -AllLanguages
```

```bash
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --all-languages
```

```zsh
./scripts/test.sh --folder 1936_add_minimum_number_of_rungs --all-languages
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
