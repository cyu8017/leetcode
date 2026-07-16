# Test harness for 3317_find_the_number_of_possible_ways_for_an_event

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language python
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language javascript
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language typescript
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language java
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language cpp
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language c
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language go
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language rust
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language kotlin
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language swift
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language ruby
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language csharp
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language scala
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language php
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm java java 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm c c 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm go go 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm rust rust 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm swift swift 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm scala scala 3317_find_the_number_of_possible_ways_for_an_event
docker compose -f docker/docker-compose.yml run --rm php php 3317_find_the_number_of_possible_ways_for_an_event
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3317_find_the_number_of_possible_ways_for_an_event` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3317_find_the_number_of_possible_ways_for_an_event` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3317_find_the_number_of_possible_ways_for_an_event` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3317_find_the_number_of_possible_ways_for_an_event` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3317_find_the_number_of_possible_ways_for_an_event` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3317_find_the_number_of_possible_ways_for_an_event` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3317_find_the_number_of_possible_ways_for_an_event` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3317_find_the_number_of_possible_ways_for_an_event` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3317_find_the_number_of_possible_ways_for_an_event` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3317_find_the_number_of_possible_ways_for_an_event` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3317_find_the_number_of_possible_ways_for_an_event` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3317_find_the_number_of_possible_ways_for_an_event` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3317_find_the_number_of_possible_ways_for_an_event` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3317_find_the_number_of_possible_ways_for_an_event` |

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
.\scripts\test.ps1 -Folder 3317_find_the_number_of_possible_ways_for_an_event -AllLanguages
```

```bash
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --all-languages
```

```zsh
./scripts/test.sh --folder 3317_find_the_number_of_possible_ways_for_an_event --all-languages
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
