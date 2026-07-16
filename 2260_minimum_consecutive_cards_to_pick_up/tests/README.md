# Test harness for 2260_minimum_consecutive_cards_to_pick_up

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language python
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language javascript
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language typescript
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language java
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language cpp
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language c
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language go
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language rust
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language kotlin
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language swift
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language ruby
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language csharp
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language scala
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language php
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm java java 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm c c 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm go go 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm rust rust 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm swift swift 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm scala scala 2260_minimum_consecutive_cards_to_pick_up
docker compose -f docker/docker-compose.yml run --rm php php 2260_minimum_consecutive_cards_to_pick_up
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2260_minimum_consecutive_cards_to_pick_up` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2260_minimum_consecutive_cards_to_pick_up` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2260_minimum_consecutive_cards_to_pick_up` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2260_minimum_consecutive_cards_to_pick_up` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2260_minimum_consecutive_cards_to_pick_up` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2260_minimum_consecutive_cards_to_pick_up` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2260_minimum_consecutive_cards_to_pick_up` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2260_minimum_consecutive_cards_to_pick_up` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2260_minimum_consecutive_cards_to_pick_up` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2260_minimum_consecutive_cards_to_pick_up` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2260_minimum_consecutive_cards_to_pick_up` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2260_minimum_consecutive_cards_to_pick_up` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2260_minimum_consecutive_cards_to_pick_up` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2260_minimum_consecutive_cards_to_pick_up` |

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
.\scripts\test.ps1 -Folder 2260_minimum_consecutive_cards_to_pick_up -AllLanguages
```

```bash
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --all-languages
```

```zsh
./scripts/test.sh --folder 2260_minimum_consecutive_cards_to_pick_up --all-languages
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
