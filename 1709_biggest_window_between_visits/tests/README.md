# Test harness for 1709_biggest_window_between_visits

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1709_biggest_window_between_visits --language python
./scripts/test.sh --folder 1709_biggest_window_between_visits --language javascript
./scripts/test.sh --folder 1709_biggest_window_between_visits --language typescript
./scripts/test.sh --folder 1709_biggest_window_between_visits --language java
./scripts/test.sh --folder 1709_biggest_window_between_visits --language cpp
./scripts/test.sh --folder 1709_biggest_window_between_visits --language c
./scripts/test.sh --folder 1709_biggest_window_between_visits --language go
./scripts/test.sh --folder 1709_biggest_window_between_visits --language rust
./scripts/test.sh --folder 1709_biggest_window_between_visits --language kotlin
./scripts/test.sh --folder 1709_biggest_window_between_visits --language swift
./scripts/test.sh --folder 1709_biggest_window_between_visits --language ruby
./scripts/test.sh --folder 1709_biggest_window_between_visits --language csharp
./scripts/test.sh --folder 1709_biggest_window_between_visits --language scala
./scripts/test.sh --folder 1709_biggest_window_between_visits --language php
./scripts/test.sh --folder 1709_biggest_window_between_visits --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1709_biggest_window_between_visits --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm java java 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm c c 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm go go 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm rust rust 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm swift swift 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm scala scala 1709_biggest_window_between_visits
docker compose -f docker/docker-compose.yml run --rm php php 1709_biggest_window_between_visits
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1709_biggest_window_between_visits` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1709_biggest_window_between_visits` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1709_biggest_window_between_visits` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1709_biggest_window_between_visits` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1709_biggest_window_between_visits` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1709_biggest_window_between_visits` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1709_biggest_window_between_visits` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1709_biggest_window_between_visits` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1709_biggest_window_between_visits` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1709_biggest_window_between_visits` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1709_biggest_window_between_visits` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1709_biggest_window_between_visits` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1709_biggest_window_between_visits` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1709_biggest_window_between_visits` |

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
.\scripts\test.ps1 -Folder 1709_biggest_window_between_visits -AllLanguages
```

```bash
./scripts/test.sh --folder 1709_biggest_window_between_visits --all-languages
```

```zsh
./scripts/test.sh --folder 1709_biggest_window_between_visits --all-languages
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
