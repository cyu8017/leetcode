# Test harness for 1733_minimum_number_of_people_to_teach

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language python
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language javascript
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language typescript
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language java
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language cpp
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language c
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language go
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language rust
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language kotlin
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language swift
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language ruby
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language csharp
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language scala
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language php
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm java java 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm c c 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm go go 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm rust rust 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm swift swift 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm scala scala 1733_minimum_number_of_people_to_teach
docker compose -f docker/docker-compose.yml run --rm php php 1733_minimum_number_of_people_to_teach
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1733_minimum_number_of_people_to_teach` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1733_minimum_number_of_people_to_teach` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1733_minimum_number_of_people_to_teach` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1733_minimum_number_of_people_to_teach` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1733_minimum_number_of_people_to_teach` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1733_minimum_number_of_people_to_teach` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1733_minimum_number_of_people_to_teach` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1733_minimum_number_of_people_to_teach` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1733_minimum_number_of_people_to_teach` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1733_minimum_number_of_people_to_teach` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1733_minimum_number_of_people_to_teach` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1733_minimum_number_of_people_to_teach` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1733_minimum_number_of_people_to_teach` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1733_minimum_number_of_people_to_teach` |

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
.\scripts\test.ps1 -Folder 1733_minimum_number_of_people_to_teach -AllLanguages
```

```bash
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --all-languages
```

```zsh
./scripts/test.sh --folder 1733_minimum_number_of_people_to_teach --all-languages
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
