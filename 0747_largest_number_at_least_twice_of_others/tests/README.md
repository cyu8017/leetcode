# Test harness for 0747_largest_number_at_least_twice_of_others

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language python
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language javascript
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language typescript
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language java
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language cpp
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language c
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language go
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language rust
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language kotlin
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language swift
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language ruby
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language csharp
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language scala
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language php
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm java java 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm c c 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm go go 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm rust rust 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm swift swift 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm scala scala 0747_largest_number_at_least_twice_of_others
docker compose -f docker/docker-compose.yml run --rm php php 0747_largest_number_at_least_twice_of_others
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0747_largest_number_at_least_twice_of_others` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0747_largest_number_at_least_twice_of_others` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0747_largest_number_at_least_twice_of_others` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0747_largest_number_at_least_twice_of_others` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0747_largest_number_at_least_twice_of_others` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0747_largest_number_at_least_twice_of_others` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0747_largest_number_at_least_twice_of_others` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0747_largest_number_at_least_twice_of_others` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0747_largest_number_at_least_twice_of_others` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0747_largest_number_at_least_twice_of_others` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0747_largest_number_at_least_twice_of_others` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0747_largest_number_at_least_twice_of_others` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0747_largest_number_at_least_twice_of_others` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0747_largest_number_at_least_twice_of_others` |

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
.\scripts\test.ps1 -Folder 0747_largest_number_at_least_twice_of_others -AllLanguages
```

```bash
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --all-languages
```

```zsh
./scripts/test.sh --folder 0747_largest_number_at_least_twice_of_others --all-languages
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
