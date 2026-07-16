# Test harness for 0871_minimum_number_of_refueling_stops

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language python
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language javascript
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language typescript
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language java
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language cpp
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language c
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language go
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language rust
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language kotlin
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language swift
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language ruby
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language csharp
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language scala
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language php
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm java java 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm c c 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm go go 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm rust rust 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm swift swift 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm scala scala 0871_minimum_number_of_refueling_stops
docker compose -f docker/docker-compose.yml run --rm php php 0871_minimum_number_of_refueling_stops
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0871_minimum_number_of_refueling_stops` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0871_minimum_number_of_refueling_stops` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0871_minimum_number_of_refueling_stops` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0871_minimum_number_of_refueling_stops` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0871_minimum_number_of_refueling_stops` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0871_minimum_number_of_refueling_stops` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0871_minimum_number_of_refueling_stops` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0871_minimum_number_of_refueling_stops` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0871_minimum_number_of_refueling_stops` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0871_minimum_number_of_refueling_stops` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0871_minimum_number_of_refueling_stops` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0871_minimum_number_of_refueling_stops` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0871_minimum_number_of_refueling_stops` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0871_minimum_number_of_refueling_stops` |

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
.\scripts\test.ps1 -Folder 0871_minimum_number_of_refueling_stops -AllLanguages
```

```bash
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --all-languages
```

```zsh
./scripts/test.sh --folder 0871_minimum_number_of_refueling_stops --all-languages
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
