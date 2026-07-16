# Test harness for 1208_get_equal_substrings_within_budget

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language python
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language javascript
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language typescript
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language java
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language cpp
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language c
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language go
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language rust
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language kotlin
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language swift
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language ruby
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language csharp
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language scala
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language php
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm java java 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm c c 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm go go 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm rust rust 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm swift swift 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm scala scala 1208_get_equal_substrings_within_budget
docker compose -f docker/docker-compose.yml run --rm php php 1208_get_equal_substrings_within_budget
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1208_get_equal_substrings_within_budget` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1208_get_equal_substrings_within_budget` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1208_get_equal_substrings_within_budget` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1208_get_equal_substrings_within_budget` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1208_get_equal_substrings_within_budget` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1208_get_equal_substrings_within_budget` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1208_get_equal_substrings_within_budget` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1208_get_equal_substrings_within_budget` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1208_get_equal_substrings_within_budget` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1208_get_equal_substrings_within_budget` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1208_get_equal_substrings_within_budget` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1208_get_equal_substrings_within_budget` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1208_get_equal_substrings_within_budget` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1208_get_equal_substrings_within_budget` |

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
.\scripts\test.ps1 -Folder 1208_get_equal_substrings_within_budget -AllLanguages
```

```bash
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --all-languages
```

```zsh
./scripts/test.sh --folder 1208_get_equal_substrings_within_budget --all-languages
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
