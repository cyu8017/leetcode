# Test harness for 1419_minimum_number_of_frogs_croaking

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language python
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language javascript
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language typescript
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language java
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language cpp
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language c
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language go
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language rust
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language kotlin
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language swift
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language ruby
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language csharp
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language scala
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language php
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm java java 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm c c 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm go go 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm rust rust 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm swift swift 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm scala scala 1419_minimum_number_of_frogs_croaking
docker compose -f docker/docker-compose.yml run --rm php php 1419_minimum_number_of_frogs_croaking
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1419_minimum_number_of_frogs_croaking` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1419_minimum_number_of_frogs_croaking` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1419_minimum_number_of_frogs_croaking` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1419_minimum_number_of_frogs_croaking` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1419_minimum_number_of_frogs_croaking` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1419_minimum_number_of_frogs_croaking` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1419_minimum_number_of_frogs_croaking` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1419_minimum_number_of_frogs_croaking` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1419_minimum_number_of_frogs_croaking` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1419_minimum_number_of_frogs_croaking` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1419_minimum_number_of_frogs_croaking` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1419_minimum_number_of_frogs_croaking` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1419_minimum_number_of_frogs_croaking` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1419_minimum_number_of_frogs_croaking` |

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
.\scripts\test.ps1 -Folder 1419_minimum_number_of_frogs_croaking -AllLanguages
```

```bash
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --all-languages
```

```zsh
./scripts/test.sh --folder 1419_minimum_number_of_frogs_croaking --all-languages
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
