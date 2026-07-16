# Test harness for 1942_the_number_of_the_smallest_unoccupied_chair

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language python
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language javascript
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language typescript
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language java
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language cpp
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language c
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language go
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language rust
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language kotlin
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language swift
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language ruby
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language csharp
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language scala
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language php
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm java java 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm c c 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm go go 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm rust rust 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm swift swift 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm scala scala 1942_the_number_of_the_smallest_unoccupied_chair
docker compose -f docker/docker-compose.yml run --rm php php 1942_the_number_of_the_smallest_unoccupied_chair
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1942_the_number_of_the_smallest_unoccupied_chair` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1942_the_number_of_the_smallest_unoccupied_chair` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1942_the_number_of_the_smallest_unoccupied_chair` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1942_the_number_of_the_smallest_unoccupied_chair` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1942_the_number_of_the_smallest_unoccupied_chair` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1942_the_number_of_the_smallest_unoccupied_chair` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1942_the_number_of_the_smallest_unoccupied_chair` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1942_the_number_of_the_smallest_unoccupied_chair` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1942_the_number_of_the_smallest_unoccupied_chair` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1942_the_number_of_the_smallest_unoccupied_chair` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1942_the_number_of_the_smallest_unoccupied_chair` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1942_the_number_of_the_smallest_unoccupied_chair` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1942_the_number_of_the_smallest_unoccupied_chair` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1942_the_number_of_the_smallest_unoccupied_chair` |

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
.\scripts\test.ps1 -Folder 1942_the_number_of_the_smallest_unoccupied_chair -AllLanguages
```

```bash
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --all-languages
```

```zsh
./scripts/test.sh --folder 1942_the_number_of_the_smallest_unoccupied_chair --all-languages
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
