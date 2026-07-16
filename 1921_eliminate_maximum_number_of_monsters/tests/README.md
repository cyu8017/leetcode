# Test harness for 1921_eliminate_maximum_number_of_monsters

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language python
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language javascript
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language typescript
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language java
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language cpp
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language c
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language go
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language rust
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language kotlin
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language swift
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language ruby
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language csharp
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language scala
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language php
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm java java 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm c c 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm go go 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm rust rust 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm swift swift 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm scala scala 1921_eliminate_maximum_number_of_monsters
docker compose -f docker/docker-compose.yml run --rm php php 1921_eliminate_maximum_number_of_monsters
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1921_eliminate_maximum_number_of_monsters` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1921_eliminate_maximum_number_of_monsters` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1921_eliminate_maximum_number_of_monsters` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1921_eliminate_maximum_number_of_monsters` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1921_eliminate_maximum_number_of_monsters` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1921_eliminate_maximum_number_of_monsters` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1921_eliminate_maximum_number_of_monsters` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1921_eliminate_maximum_number_of_monsters` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1921_eliminate_maximum_number_of_monsters` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1921_eliminate_maximum_number_of_monsters` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1921_eliminate_maximum_number_of_monsters` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1921_eliminate_maximum_number_of_monsters` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1921_eliminate_maximum_number_of_monsters` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1921_eliminate_maximum_number_of_monsters` |

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
.\scripts\test.ps1 -Folder 1921_eliminate_maximum_number_of_monsters -AllLanguages
```

```bash
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --all-languages
```

```zsh
./scripts/test.sh --folder 1921_eliminate_maximum_number_of_monsters --all-languages
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
