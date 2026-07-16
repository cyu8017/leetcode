# Test harness for 2446_determine_if_two_events_have_conflict

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language python
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language javascript
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language typescript
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language java
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language cpp
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language c
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language go
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language rust
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language kotlin
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language swift
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language ruby
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language csharp
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language scala
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language php
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm java java 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm c c 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm go go 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm rust rust 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm swift swift 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm scala scala 2446_determine_if_two_events_have_conflict
docker compose -f docker/docker-compose.yml run --rm php php 2446_determine_if_two_events_have_conflict
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2446_determine_if_two_events_have_conflict` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2446_determine_if_two_events_have_conflict` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2446_determine_if_two_events_have_conflict` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2446_determine_if_two_events_have_conflict` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2446_determine_if_two_events_have_conflict` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2446_determine_if_two_events_have_conflict` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2446_determine_if_two_events_have_conflict` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2446_determine_if_two_events_have_conflict` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2446_determine_if_two_events_have_conflict` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2446_determine_if_two_events_have_conflict` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2446_determine_if_two_events_have_conflict` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2446_determine_if_two_events_have_conflict` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2446_determine_if_two_events_have_conflict` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2446_determine_if_two_events_have_conflict` |

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
.\scripts\test.ps1 -Folder 2446_determine_if_two_events_have_conflict -AllLanguages
```

```bash
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --all-languages
```

```zsh
./scripts/test.sh --folder 2446_determine_if_two_events_have_conflict --all-languages
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
