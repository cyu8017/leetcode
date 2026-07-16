# Test harness for 0528_random_pick_with_weight

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0528_random_pick_with_weight --language python
./scripts/test.sh --folder 0528_random_pick_with_weight --language javascript
./scripts/test.sh --folder 0528_random_pick_with_weight --language typescript
./scripts/test.sh --folder 0528_random_pick_with_weight --language java
./scripts/test.sh --folder 0528_random_pick_with_weight --language cpp
./scripts/test.sh --folder 0528_random_pick_with_weight --language c
./scripts/test.sh --folder 0528_random_pick_with_weight --language go
./scripts/test.sh --folder 0528_random_pick_with_weight --language rust
./scripts/test.sh --folder 0528_random_pick_with_weight --language kotlin
./scripts/test.sh --folder 0528_random_pick_with_weight --language swift
./scripts/test.sh --folder 0528_random_pick_with_weight --language ruby
./scripts/test.sh --folder 0528_random_pick_with_weight --language csharp
./scripts/test.sh --folder 0528_random_pick_with_weight --language scala
./scripts/test.sh --folder 0528_random_pick_with_weight --language php
./scripts/test.sh --folder 0528_random_pick_with_weight --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0528_random_pick_with_weight --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm java java 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm c c 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm go go 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm rust rust 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm swift swift 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm scala scala 0528_random_pick_with_weight
docker compose -f docker/docker-compose.yml run --rm php php 0528_random_pick_with_weight
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0528_random_pick_with_weight` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0528_random_pick_with_weight` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0528_random_pick_with_weight` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0528_random_pick_with_weight` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0528_random_pick_with_weight` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0528_random_pick_with_weight` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0528_random_pick_with_weight` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0528_random_pick_with_weight` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0528_random_pick_with_weight` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0528_random_pick_with_weight` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0528_random_pick_with_weight` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0528_random_pick_with_weight` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0528_random_pick_with_weight` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0528_random_pick_with_weight` |

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
.\scripts\test.ps1 -Folder 0528_random_pick_with_weight -AllLanguages
```

```bash
./scripts/test.sh --folder 0528_random_pick_with_weight --all-languages
```

```zsh
./scripts/test.sh --folder 0528_random_pick_with_weight --all-languages
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
