# Test harness for 0553_optimal_division

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0553_optimal_division -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0553_optimal_division --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0553_optimal_division --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0553_optimal_division --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0553_optimal_division --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0553_optimal_division --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0553_optimal_division --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0553_optimal_division --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0553_optimal_division --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0553_optimal_division --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0553_optimal_division --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0553_optimal_division --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0553_optimal_division --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0553_optimal_division --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0553_optimal_division --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0553_optimal_division --language python
./scripts/test.sh --folder 0553_optimal_division --language javascript
./scripts/test.sh --folder 0553_optimal_division --language typescript
./scripts/test.sh --folder 0553_optimal_division --language java
./scripts/test.sh --folder 0553_optimal_division --language cpp
./scripts/test.sh --folder 0553_optimal_division --language c
./scripts/test.sh --folder 0553_optimal_division --language go
./scripts/test.sh --folder 0553_optimal_division --language rust
./scripts/test.sh --folder 0553_optimal_division --language kotlin
./scripts/test.sh --folder 0553_optimal_division --language swift
./scripts/test.sh --folder 0553_optimal_division --language ruby
./scripts/test.sh --folder 0553_optimal_division --language csharp
./scripts/test.sh --folder 0553_optimal_division --language scala
./scripts/test.sh --folder 0553_optimal_division --language php
./scripts/test.sh --folder 0553_optimal_division --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0553_optimal_division --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0553_optimal_division --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0553_optimal_division --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0553_optimal_division --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0553_optimal_division --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0553_optimal_division --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0553_optimal_division --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0553_optimal_division --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0553_optimal_division --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0553_optimal_division --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0553_optimal_division --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0553_optimal_division --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0553_optimal_division --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0553_optimal_division --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm java java 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm c c 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm go go 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm rust rust 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm swift swift 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm scala scala 0553_optimal_division
docker compose -f docker/docker-compose.yml run --rm php php 0553_optimal_division
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0553_optimal_division` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0553_optimal_division` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0553_optimal_division` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0553_optimal_division` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0553_optimal_division` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0553_optimal_division` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0553_optimal_division` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0553_optimal_division` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0553_optimal_division` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0553_optimal_division` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0553_optimal_division` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0553_optimal_division` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0553_optimal_division` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0553_optimal_division` |

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
.\scripts\test.ps1 -Folder 0553_optimal_division -AllLanguages
```

```bash
./scripts/test.sh --folder 0553_optimal_division --all-languages
```

```zsh
./scripts/test.sh --folder 0553_optimal_division --all-languages
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
