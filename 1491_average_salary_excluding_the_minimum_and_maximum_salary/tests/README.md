# Test harness for 1491_average_salary_excluding_the_minimum_and_maximum_salary

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language python
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language javascript
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language typescript
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language java
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language cpp
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language c
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language go
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language rust
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language kotlin
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language swift
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language ruby
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language csharp
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language scala
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language php
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm java java 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm c c 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm go go 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm rust rust 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm swift swift 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm scala scala 1491_average_salary_excluding_the_minimum_and_maximum_salary
docker compose -f docker/docker-compose.yml run --rm php php 1491_average_salary_excluding_the_minimum_and_maximum_salary
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1491_average_salary_excluding_the_minimum_and_maximum_salary` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1491_average_salary_excluding_the_minimum_and_maximum_salary` |

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
.\scripts\test.ps1 -Folder 1491_average_salary_excluding_the_minimum_and_maximum_salary -AllLanguages
```

```bash
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --all-languages
```

```zsh
./scripts/test.sh --folder 1491_average_salary_excluding_the_minimum_and_maximum_salary --all-languages
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
