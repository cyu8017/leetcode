# Test harness for 0252_meeting_rooms

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0252_meeting_rooms -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0252_meeting_rooms --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0252_meeting_rooms --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0252_meeting_rooms --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0252_meeting_rooms --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0252_meeting_rooms --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0252_meeting_rooms --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0252_meeting_rooms --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0252_meeting_rooms --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0252_meeting_rooms --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0252_meeting_rooms --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0252_meeting_rooms --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0252_meeting_rooms --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0252_meeting_rooms --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0252_meeting_rooms --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0252_meeting_rooms --language python
./scripts/test.sh --folder 0252_meeting_rooms --language javascript
./scripts/test.sh --folder 0252_meeting_rooms --language typescript
./scripts/test.sh --folder 0252_meeting_rooms --language java
./scripts/test.sh --folder 0252_meeting_rooms --language cpp
./scripts/test.sh --folder 0252_meeting_rooms --language c
./scripts/test.sh --folder 0252_meeting_rooms --language go
./scripts/test.sh --folder 0252_meeting_rooms --language rust
./scripts/test.sh --folder 0252_meeting_rooms --language kotlin
./scripts/test.sh --folder 0252_meeting_rooms --language swift
./scripts/test.sh --folder 0252_meeting_rooms --language ruby
./scripts/test.sh --folder 0252_meeting_rooms --language csharp
./scripts/test.sh --folder 0252_meeting_rooms --language scala
./scripts/test.sh --folder 0252_meeting_rooms --language php
./scripts/test.sh --folder 0252_meeting_rooms --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0252_meeting_rooms --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0252_meeting_rooms --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0252_meeting_rooms --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0252_meeting_rooms --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0252_meeting_rooms --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0252_meeting_rooms --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0252_meeting_rooms --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0252_meeting_rooms --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0252_meeting_rooms --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0252_meeting_rooms --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0252_meeting_rooms --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0252_meeting_rooms --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0252_meeting_rooms --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0252_meeting_rooms --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm java java 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm c c 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm go go 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm rust rust 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm swift swift 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm scala scala 0252_meeting_rooms
docker compose -f docker/docker-compose.yml run --rm php php 0252_meeting_rooms
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0252_meeting_rooms` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0252_meeting_rooms` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0252_meeting_rooms` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0252_meeting_rooms` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0252_meeting_rooms` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0252_meeting_rooms` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0252_meeting_rooms` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0252_meeting_rooms` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0252_meeting_rooms` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0252_meeting_rooms` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0252_meeting_rooms` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0252_meeting_rooms` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0252_meeting_rooms` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0252_meeting_rooms` |

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
.\scripts\test.ps1 -Folder 0252_meeting_rooms -AllLanguages
```

```bash
./scripts/test.sh --folder 0252_meeting_rooms --all-languages
```

```zsh
./scripts/test.sh --folder 0252_meeting_rooms --all-languages
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
