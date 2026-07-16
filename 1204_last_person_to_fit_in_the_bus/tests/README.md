# Test harness for 1204_last_person_to_fit_in_the_bus

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language python
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language javascript
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language typescript
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language java
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language cpp
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language c
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language go
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language rust
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language kotlin
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language swift
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language ruby
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language csharp
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language scala
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language php
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm java java 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm c c 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm go go 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm rust rust 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm swift swift 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm scala scala 1204_last_person_to_fit_in_the_bus
docker compose -f docker/docker-compose.yml run --rm php php 1204_last_person_to_fit_in_the_bus
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1204_last_person_to_fit_in_the_bus` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1204_last_person_to_fit_in_the_bus` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1204_last_person_to_fit_in_the_bus` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1204_last_person_to_fit_in_the_bus` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1204_last_person_to_fit_in_the_bus` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1204_last_person_to_fit_in_the_bus` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1204_last_person_to_fit_in_the_bus` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1204_last_person_to_fit_in_the_bus` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1204_last_person_to_fit_in_the_bus` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1204_last_person_to_fit_in_the_bus` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1204_last_person_to_fit_in_the_bus` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1204_last_person_to_fit_in_the_bus` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1204_last_person_to_fit_in_the_bus` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1204_last_person_to_fit_in_the_bus` |

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
.\scripts\test.ps1 -Folder 1204_last_person_to_fit_in_the_bus -AllLanguages
```

```bash
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --all-languages
```

```zsh
./scripts/test.sh --folder 1204_last_person_to_fit_in_the_bus --all-languages
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
