# Test harness for 2358_maximum_number_of_groups_entering_a_competition

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language python
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language javascript
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language typescript
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language java
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language cpp
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language c
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language go
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language rust
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language kotlin
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language swift
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language ruby
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language csharp
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language scala
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language php
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm java java 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm c c 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm go go 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm rust rust 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm swift swift 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm scala scala 2358_maximum_number_of_groups_entering_a_competition
docker compose -f docker/docker-compose.yml run --rm php php 2358_maximum_number_of_groups_entering_a_competition
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2358_maximum_number_of_groups_entering_a_competition` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2358_maximum_number_of_groups_entering_a_competition` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2358_maximum_number_of_groups_entering_a_competition` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2358_maximum_number_of_groups_entering_a_competition` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2358_maximum_number_of_groups_entering_a_competition` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2358_maximum_number_of_groups_entering_a_competition` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2358_maximum_number_of_groups_entering_a_competition` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2358_maximum_number_of_groups_entering_a_competition` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2358_maximum_number_of_groups_entering_a_competition` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2358_maximum_number_of_groups_entering_a_competition` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2358_maximum_number_of_groups_entering_a_competition` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2358_maximum_number_of_groups_entering_a_competition` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2358_maximum_number_of_groups_entering_a_competition` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2358_maximum_number_of_groups_entering_a_competition` |

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
.\scripts\test.ps1 -Folder 2358_maximum_number_of_groups_entering_a_competition -AllLanguages
```

```bash
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --all-languages
```

```zsh
./scripts/test.sh --folder 2358_maximum_number_of_groups_entering_a_competition --all-languages
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
