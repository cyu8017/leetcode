# Test harness for 0846_hand_of_straights

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0846_hand_of_straights -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0846_hand_of_straights --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0846_hand_of_straights --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0846_hand_of_straights --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0846_hand_of_straights --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0846_hand_of_straights --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0846_hand_of_straights --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0846_hand_of_straights --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0846_hand_of_straights --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0846_hand_of_straights --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0846_hand_of_straights --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0846_hand_of_straights --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0846_hand_of_straights --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0846_hand_of_straights --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0846_hand_of_straights --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0846_hand_of_straights --language python
./scripts/test.sh --folder 0846_hand_of_straights --language javascript
./scripts/test.sh --folder 0846_hand_of_straights --language typescript
./scripts/test.sh --folder 0846_hand_of_straights --language java
./scripts/test.sh --folder 0846_hand_of_straights --language cpp
./scripts/test.sh --folder 0846_hand_of_straights --language c
./scripts/test.sh --folder 0846_hand_of_straights --language go
./scripts/test.sh --folder 0846_hand_of_straights --language rust
./scripts/test.sh --folder 0846_hand_of_straights --language kotlin
./scripts/test.sh --folder 0846_hand_of_straights --language swift
./scripts/test.sh --folder 0846_hand_of_straights --language ruby
./scripts/test.sh --folder 0846_hand_of_straights --language csharp
./scripts/test.sh --folder 0846_hand_of_straights --language scala
./scripts/test.sh --folder 0846_hand_of_straights --language php
./scripts/test.sh --folder 0846_hand_of_straights --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0846_hand_of_straights --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0846_hand_of_straights --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0846_hand_of_straights --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0846_hand_of_straights --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0846_hand_of_straights --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0846_hand_of_straights --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0846_hand_of_straights --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0846_hand_of_straights --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0846_hand_of_straights --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0846_hand_of_straights --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0846_hand_of_straights --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0846_hand_of_straights --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0846_hand_of_straights --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0846_hand_of_straights --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm java java 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm c c 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm go go 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm rust rust 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm swift swift 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm scala scala 0846_hand_of_straights
docker compose -f docker/docker-compose.yml run --rm php php 0846_hand_of_straights
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0846_hand_of_straights` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0846_hand_of_straights` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0846_hand_of_straights` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0846_hand_of_straights` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0846_hand_of_straights` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0846_hand_of_straights` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0846_hand_of_straights` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0846_hand_of_straights` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0846_hand_of_straights` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0846_hand_of_straights` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0846_hand_of_straights` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0846_hand_of_straights` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0846_hand_of_straights` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0846_hand_of_straights` |

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
.\scripts\test.ps1 -Folder 0846_hand_of_straights -AllLanguages
```

```bash
./scripts/test.sh --folder 0846_hand_of_straights --all-languages
```

```zsh
./scripts/test.sh --folder 0846_hand_of_straights --all-languages
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
