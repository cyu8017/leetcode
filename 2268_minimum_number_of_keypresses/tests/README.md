# Test harness for 2268_minimum_number_of_keypresses

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language python
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language javascript
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language typescript
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language java
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language cpp
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language c
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language go
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language rust
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language kotlin
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language swift
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language ruby
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language csharp
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language scala
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language php
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2268_minimum_number_of_keypresses --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm java java 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm c c 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm go go 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm rust rust 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm swift swift 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm scala scala 2268_minimum_number_of_keypresses
docker compose -f docker/docker-compose.yml run --rm php php 2268_minimum_number_of_keypresses
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2268_minimum_number_of_keypresses` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2268_minimum_number_of_keypresses` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2268_minimum_number_of_keypresses` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2268_minimum_number_of_keypresses` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2268_minimum_number_of_keypresses` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2268_minimum_number_of_keypresses` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2268_minimum_number_of_keypresses` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2268_minimum_number_of_keypresses` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2268_minimum_number_of_keypresses` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2268_minimum_number_of_keypresses` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2268_minimum_number_of_keypresses` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2268_minimum_number_of_keypresses` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2268_minimum_number_of_keypresses` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2268_minimum_number_of_keypresses` |

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
.\scripts\test.ps1 -Folder 2268_minimum_number_of_keypresses -AllLanguages
```

```bash
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --all-languages
```

```zsh
./scripts/test.sh --folder 2268_minimum_number_of_keypresses --all-languages
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
