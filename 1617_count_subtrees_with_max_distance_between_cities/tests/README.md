# Test harness for 1617_count_subtrees_with_max_distance_between_cities

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language python
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language javascript
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language typescript
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language java
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language cpp
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language c
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language go
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language rust
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language kotlin
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language swift
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language ruby
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language csharp
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language scala
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language php
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm java java 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm c c 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm go go 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm rust rust 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm swift swift 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm scala scala 1617_count_subtrees_with_max_distance_between_cities
docker compose -f docker/docker-compose.yml run --rm php php 1617_count_subtrees_with_max_distance_between_cities
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1617_count_subtrees_with_max_distance_between_cities` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1617_count_subtrees_with_max_distance_between_cities` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1617_count_subtrees_with_max_distance_between_cities` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1617_count_subtrees_with_max_distance_between_cities` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1617_count_subtrees_with_max_distance_between_cities` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1617_count_subtrees_with_max_distance_between_cities` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1617_count_subtrees_with_max_distance_between_cities` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1617_count_subtrees_with_max_distance_between_cities` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1617_count_subtrees_with_max_distance_between_cities` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1617_count_subtrees_with_max_distance_between_cities` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1617_count_subtrees_with_max_distance_between_cities` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1617_count_subtrees_with_max_distance_between_cities` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1617_count_subtrees_with_max_distance_between_cities` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1617_count_subtrees_with_max_distance_between_cities` |

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
.\scripts\test.ps1 -Folder 1617_count_subtrees_with_max_distance_between_cities -AllLanguages
```

```bash
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --all-languages
```

```zsh
./scripts/test.sh --folder 1617_count_subtrees_with_max_distance_between_cities --all-languages
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
