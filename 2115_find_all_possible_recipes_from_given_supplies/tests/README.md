# Test harness for 2115_find_all_possible_recipes_from_given_supplies

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language python
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language javascript
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language typescript
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language java
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language cpp
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language c
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language go
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language rust
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language kotlin
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language swift
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language ruby
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language csharp
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language scala
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language php
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm java java 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm c c 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm go go 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm rust rust 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm swift swift 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm scala scala 2115_find_all_possible_recipes_from_given_supplies
docker compose -f docker/docker-compose.yml run --rm php php 2115_find_all_possible_recipes_from_given_supplies
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2115_find_all_possible_recipes_from_given_supplies` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2115_find_all_possible_recipes_from_given_supplies` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2115_find_all_possible_recipes_from_given_supplies` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2115_find_all_possible_recipes_from_given_supplies` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2115_find_all_possible_recipes_from_given_supplies` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2115_find_all_possible_recipes_from_given_supplies` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2115_find_all_possible_recipes_from_given_supplies` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2115_find_all_possible_recipes_from_given_supplies` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2115_find_all_possible_recipes_from_given_supplies` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2115_find_all_possible_recipes_from_given_supplies` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2115_find_all_possible_recipes_from_given_supplies` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2115_find_all_possible_recipes_from_given_supplies` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2115_find_all_possible_recipes_from_given_supplies` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2115_find_all_possible_recipes_from_given_supplies` |

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
.\scripts\test.ps1 -Folder 2115_find_all_possible_recipes_from_given_supplies -AllLanguages
```

```bash
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --all-languages
```

```zsh
./scripts/test.sh --folder 2115_find_all_possible_recipes_from_given_supplies --all-languages
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
