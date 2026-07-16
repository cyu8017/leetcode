# Test harness for 1992_find_all_groups_of_farmland

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language python
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language javascript
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language typescript
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language java
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language cpp
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language c
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language go
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language rust
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language kotlin
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language swift
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language ruby
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language csharp
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language scala
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language php
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1992_find_all_groups_of_farmland --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm java java 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm c c 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm go go 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm rust rust 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm swift swift 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm scala scala 1992_find_all_groups_of_farmland
docker compose -f docker/docker-compose.yml run --rm php php 1992_find_all_groups_of_farmland
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1992_find_all_groups_of_farmland` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1992_find_all_groups_of_farmland` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1992_find_all_groups_of_farmland` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1992_find_all_groups_of_farmland` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1992_find_all_groups_of_farmland` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1992_find_all_groups_of_farmland` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1992_find_all_groups_of_farmland` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1992_find_all_groups_of_farmland` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1992_find_all_groups_of_farmland` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1992_find_all_groups_of_farmland` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1992_find_all_groups_of_farmland` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1992_find_all_groups_of_farmland` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1992_find_all_groups_of_farmland` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1992_find_all_groups_of_farmland` |

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
.\scripts\test.ps1 -Folder 1992_find_all_groups_of_farmland -AllLanguages
```

```bash
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --all-languages
```

```zsh
./scripts/test.sh --folder 1992_find_all_groups_of_farmland --all-languages
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
