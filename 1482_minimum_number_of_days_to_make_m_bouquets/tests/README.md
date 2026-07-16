# Test harness for 1482_minimum_number_of_days_to_make_m_bouquets

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language python
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language javascript
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language typescript
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language java
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language cpp
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language c
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language go
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language rust
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language kotlin
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language swift
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language ruby
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language csharp
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language scala
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language php
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm java java 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm c c 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm go go 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm rust rust 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm swift swift 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm scala scala 1482_minimum_number_of_days_to_make_m_bouquets
docker compose -f docker/docker-compose.yml run --rm php php 1482_minimum_number_of_days_to_make_m_bouquets
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1482_minimum_number_of_days_to_make_m_bouquets` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1482_minimum_number_of_days_to_make_m_bouquets` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1482_minimum_number_of_days_to_make_m_bouquets` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1482_minimum_number_of_days_to_make_m_bouquets` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1482_minimum_number_of_days_to_make_m_bouquets` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1482_minimum_number_of_days_to_make_m_bouquets` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1482_minimum_number_of_days_to_make_m_bouquets` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1482_minimum_number_of_days_to_make_m_bouquets` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1482_minimum_number_of_days_to_make_m_bouquets` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1482_minimum_number_of_days_to_make_m_bouquets` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1482_minimum_number_of_days_to_make_m_bouquets` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1482_minimum_number_of_days_to_make_m_bouquets` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1482_minimum_number_of_days_to_make_m_bouquets` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1482_minimum_number_of_days_to_make_m_bouquets` |

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
.\scripts\test.ps1 -Folder 1482_minimum_number_of_days_to_make_m_bouquets -AllLanguages
```

```bash
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --all-languages
```

```zsh
./scripts/test.sh --folder 1482_minimum_number_of_days_to_make_m_bouquets --all-languages
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
