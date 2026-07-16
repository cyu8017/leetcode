# Test harness for 0245_shortest_word_distance_iii

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language python
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language javascript
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language typescript
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language java
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language cpp
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language c
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language go
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language rust
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language kotlin
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language swift
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language ruby
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language csharp
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language scala
./scripts/test.sh --folder 0245_shortest_word_distance_iii --language php
./scripts/test.sh --folder 0245_shortest_word_distance_iii --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0245_shortest_word_distance_iii --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm java java 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm c c 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm go go 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm rust rust 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm swift swift 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm scala scala 0245_shortest_word_distance_iii
docker compose -f docker/docker-compose.yml run --rm php php 0245_shortest_word_distance_iii
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0245_shortest_word_distance_iii` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0245_shortest_word_distance_iii` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0245_shortest_word_distance_iii` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0245_shortest_word_distance_iii` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0245_shortest_word_distance_iii` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0245_shortest_word_distance_iii` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0245_shortest_word_distance_iii` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0245_shortest_word_distance_iii` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0245_shortest_word_distance_iii` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0245_shortest_word_distance_iii` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0245_shortest_word_distance_iii` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0245_shortest_word_distance_iii` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0245_shortest_word_distance_iii` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0245_shortest_word_distance_iii` |

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
.\scripts\test.ps1 -Folder 0245_shortest_word_distance_iii -AllLanguages
```

```bash
./scripts/test.sh --folder 0245_shortest_word_distance_iii --all-languages
```

```zsh
./scripts/test.sh --folder 0245_shortest_word_distance_iii --all-languages
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
