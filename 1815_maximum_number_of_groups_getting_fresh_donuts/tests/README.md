# Test harness for 1815_maximum_number_of_groups_getting_fresh_donuts

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language python
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language javascript
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language typescript
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language java
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language cpp
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language c
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language go
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language rust
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language kotlin
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language swift
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language ruby
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language csharp
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language scala
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language php
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm java java 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm c c 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm go go 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm rust rust 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm swift swift 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm scala scala 1815_maximum_number_of_groups_getting_fresh_donuts
docker compose -f docker/docker-compose.yml run --rm php php 1815_maximum_number_of_groups_getting_fresh_donuts
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1815_maximum_number_of_groups_getting_fresh_donuts` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1815_maximum_number_of_groups_getting_fresh_donuts` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1815_maximum_number_of_groups_getting_fresh_donuts` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1815_maximum_number_of_groups_getting_fresh_donuts` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1815_maximum_number_of_groups_getting_fresh_donuts` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1815_maximum_number_of_groups_getting_fresh_donuts` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1815_maximum_number_of_groups_getting_fresh_donuts` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1815_maximum_number_of_groups_getting_fresh_donuts` |

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
.\scripts\test.ps1 -Folder 1815_maximum_number_of_groups_getting_fresh_donuts -AllLanguages
```

```bash
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --all-languages
```

```zsh
./scripts/test.sh --folder 1815_maximum_number_of_groups_getting_fresh_donuts --all-languages
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
