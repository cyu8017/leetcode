# Test harness for 2694_event_emitter

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2694_event_emitter -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2694_event_emitter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2694_event_emitter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2694_event_emitter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2694_event_emitter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2694_event_emitter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2694_event_emitter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2694_event_emitter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2694_event_emitter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2694_event_emitter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2694_event_emitter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2694_event_emitter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2694_event_emitter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2694_event_emitter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2694_event_emitter --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2694_event_emitter --language python
./scripts/test.sh --folder 2694_event_emitter --language javascript
./scripts/test.sh --folder 2694_event_emitter --language typescript
./scripts/test.sh --folder 2694_event_emitter --language java
./scripts/test.sh --folder 2694_event_emitter --language cpp
./scripts/test.sh --folder 2694_event_emitter --language c
./scripts/test.sh --folder 2694_event_emitter --language go
./scripts/test.sh --folder 2694_event_emitter --language rust
./scripts/test.sh --folder 2694_event_emitter --language kotlin
./scripts/test.sh --folder 2694_event_emitter --language swift
./scripts/test.sh --folder 2694_event_emitter --language ruby
./scripts/test.sh --folder 2694_event_emitter --language csharp
./scripts/test.sh --folder 2694_event_emitter --language scala
./scripts/test.sh --folder 2694_event_emitter --language php
./scripts/test.sh --folder 2694_event_emitter --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2694_event_emitter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2694_event_emitter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2694_event_emitter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2694_event_emitter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2694_event_emitter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2694_event_emitter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2694_event_emitter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2694_event_emitter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2694_event_emitter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2694_event_emitter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2694_event_emitter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2694_event_emitter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2694_event_emitter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2694_event_emitter --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm java java 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm c c 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm go go 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm rust rust 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm swift swift 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm scala scala 2694_event_emitter
docker compose -f docker/docker-compose.yml run --rm php php 2694_event_emitter
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2694_event_emitter` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2694_event_emitter` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2694_event_emitter` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2694_event_emitter` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2694_event_emitter` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2694_event_emitter` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2694_event_emitter` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2694_event_emitter` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2694_event_emitter` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2694_event_emitter` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2694_event_emitter` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2694_event_emitter` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2694_event_emitter` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2694_event_emitter` |

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
.\scripts\test.ps1 -Folder 2694_event_emitter -AllLanguages
```

```bash
./scripts/test.sh --folder 2694_event_emitter --all-languages
```

```zsh
./scripts/test.sh --folder 2694_event_emitter --all-languages
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
