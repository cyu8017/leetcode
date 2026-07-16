# Test harness for 2426_number_of_pairs_satisfying_inequality

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language python
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language javascript
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language typescript
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language java
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language cpp
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language c
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language go
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language rust
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language kotlin
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language swift
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language ruby
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language csharp
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language scala
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language php
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm java java 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm c c 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm go go 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm rust rust 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm swift swift 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm scala scala 2426_number_of_pairs_satisfying_inequality
docker compose -f docker/docker-compose.yml run --rm php php 2426_number_of_pairs_satisfying_inequality
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2426_number_of_pairs_satisfying_inequality` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2426_number_of_pairs_satisfying_inequality` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2426_number_of_pairs_satisfying_inequality` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2426_number_of_pairs_satisfying_inequality` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2426_number_of_pairs_satisfying_inequality` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2426_number_of_pairs_satisfying_inequality` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2426_number_of_pairs_satisfying_inequality` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2426_number_of_pairs_satisfying_inequality` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2426_number_of_pairs_satisfying_inequality` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2426_number_of_pairs_satisfying_inequality` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2426_number_of_pairs_satisfying_inequality` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2426_number_of_pairs_satisfying_inequality` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2426_number_of_pairs_satisfying_inequality` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2426_number_of_pairs_satisfying_inequality` |

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
.\scripts\test.ps1 -Folder 2426_number_of_pairs_satisfying_inequality -AllLanguages
```

```bash
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --all-languages
```

```zsh
./scripts/test.sh --folder 2426_number_of_pairs_satisfying_inequality --all-languages
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
