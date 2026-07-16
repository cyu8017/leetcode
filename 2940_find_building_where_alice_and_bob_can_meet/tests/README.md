# Test harness for 2940_find_building_where_alice_and_bob_can_meet

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language python
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language javascript
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language typescript
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language java
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language cpp
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language c
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language go
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language rust
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language kotlin
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language swift
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language ruby
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language csharp
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language scala
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language php
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm java java 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm c c 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm go go 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm rust rust 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm swift swift 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm scala scala 2940_find_building_where_alice_and_bob_can_meet
docker compose -f docker/docker-compose.yml run --rm php php 2940_find_building_where_alice_and_bob_can_meet
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2940_find_building_where_alice_and_bob_can_meet` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2940_find_building_where_alice_and_bob_can_meet` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2940_find_building_where_alice_and_bob_can_meet` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2940_find_building_where_alice_and_bob_can_meet` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2940_find_building_where_alice_and_bob_can_meet` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2940_find_building_where_alice_and_bob_can_meet` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2940_find_building_where_alice_and_bob_can_meet` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2940_find_building_where_alice_and_bob_can_meet` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2940_find_building_where_alice_and_bob_can_meet` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2940_find_building_where_alice_and_bob_can_meet` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2940_find_building_where_alice_and_bob_can_meet` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2940_find_building_where_alice_and_bob_can_meet` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2940_find_building_where_alice_and_bob_can_meet` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2940_find_building_where_alice_and_bob_can_meet` |

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
.\scripts\test.ps1 -Folder 2940_find_building_where_alice_and_bob_can_meet -AllLanguages
```

```bash
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --all-languages
```

```zsh
./scripts/test.sh --folder 2940_find_building_where_alice_and_bob_can_meet --all-languages
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
