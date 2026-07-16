# Test harness for 1135_connecting_cities_with_minimum_cost

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language python
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language javascript
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language typescript
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language java
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language cpp
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language c
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language go
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language rust
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language kotlin
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language swift
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language ruby
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language csharp
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language scala
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language php
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm java java 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm c c 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm go go 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm rust rust 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm swift swift 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm scala scala 1135_connecting_cities_with_minimum_cost
docker compose -f docker/docker-compose.yml run --rm php php 1135_connecting_cities_with_minimum_cost
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1135_connecting_cities_with_minimum_cost` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1135_connecting_cities_with_minimum_cost` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1135_connecting_cities_with_minimum_cost` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1135_connecting_cities_with_minimum_cost` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1135_connecting_cities_with_minimum_cost` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1135_connecting_cities_with_minimum_cost` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1135_connecting_cities_with_minimum_cost` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1135_connecting_cities_with_minimum_cost` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1135_connecting_cities_with_minimum_cost` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1135_connecting_cities_with_minimum_cost` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1135_connecting_cities_with_minimum_cost` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1135_connecting_cities_with_minimum_cost` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1135_connecting_cities_with_minimum_cost` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1135_connecting_cities_with_minimum_cost` |

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
.\scripts\test.ps1 -Folder 1135_connecting_cities_with_minimum_cost -AllLanguages
```

```bash
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --all-languages
```

```zsh
./scripts/test.sh --folder 1135_connecting_cities_with_minimum_cost --all-languages
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
