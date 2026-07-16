# Test harness for 1094_car_pooling

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1094_car_pooling -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1094_car_pooling --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1094_car_pooling --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1094_car_pooling --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1094_car_pooling --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1094_car_pooling --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1094_car_pooling --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1094_car_pooling --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1094_car_pooling --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1094_car_pooling --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1094_car_pooling --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1094_car_pooling --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1094_car_pooling --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1094_car_pooling --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1094_car_pooling --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1094_car_pooling --language python
./scripts/test.sh --folder 1094_car_pooling --language javascript
./scripts/test.sh --folder 1094_car_pooling --language typescript
./scripts/test.sh --folder 1094_car_pooling --language java
./scripts/test.sh --folder 1094_car_pooling --language cpp
./scripts/test.sh --folder 1094_car_pooling --language c
./scripts/test.sh --folder 1094_car_pooling --language go
./scripts/test.sh --folder 1094_car_pooling --language rust
./scripts/test.sh --folder 1094_car_pooling --language kotlin
./scripts/test.sh --folder 1094_car_pooling --language swift
./scripts/test.sh --folder 1094_car_pooling --language ruby
./scripts/test.sh --folder 1094_car_pooling --language csharp
./scripts/test.sh --folder 1094_car_pooling --language scala
./scripts/test.sh --folder 1094_car_pooling --language php
./scripts/test.sh --folder 1094_car_pooling --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1094_car_pooling --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1094_car_pooling --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1094_car_pooling --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1094_car_pooling --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1094_car_pooling --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1094_car_pooling --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1094_car_pooling --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1094_car_pooling --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1094_car_pooling --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1094_car_pooling --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1094_car_pooling --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1094_car_pooling --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1094_car_pooling --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1094_car_pooling --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm java java 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm c c 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm go go 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm rust rust 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm swift swift 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm scala scala 1094_car_pooling
docker compose -f docker/docker-compose.yml run --rm php php 1094_car_pooling
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1094_car_pooling` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1094_car_pooling` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1094_car_pooling` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1094_car_pooling` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1094_car_pooling` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1094_car_pooling` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1094_car_pooling` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1094_car_pooling` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1094_car_pooling` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1094_car_pooling` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1094_car_pooling` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1094_car_pooling` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1094_car_pooling` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1094_car_pooling` |

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
.\scripts\test.ps1 -Folder 1094_car_pooling -AllLanguages
```

```bash
./scripts/test.sh --folder 1094_car_pooling --all-languages
```

```zsh
./scripts/test.sh --folder 1094_car_pooling --all-languages
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
