# Test harness for 2621_sleep

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2621_sleep -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2621_sleep -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2621_sleep -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2621_sleep -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2621_sleep -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2621_sleep -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2621_sleep -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2621_sleep -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2621_sleep -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2621_sleep -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2621_sleep -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2621_sleep -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2621_sleep -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2621_sleep -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2621_sleep --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2621_sleep --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2621_sleep --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2621_sleep --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2621_sleep --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2621_sleep --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2621_sleep --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2621_sleep --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2621_sleep --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2621_sleep --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2621_sleep --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2621_sleep --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2621_sleep --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2621_sleep --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2621_sleep --language python
./scripts/test.sh --folder 2621_sleep --language javascript
./scripts/test.sh --folder 2621_sleep --language typescript
./scripts/test.sh --folder 2621_sleep --language java
./scripts/test.sh --folder 2621_sleep --language cpp
./scripts/test.sh --folder 2621_sleep --language c
./scripts/test.sh --folder 2621_sleep --language go
./scripts/test.sh --folder 2621_sleep --language rust
./scripts/test.sh --folder 2621_sleep --language kotlin
./scripts/test.sh --folder 2621_sleep --language swift
./scripts/test.sh --folder 2621_sleep --language ruby
./scripts/test.sh --folder 2621_sleep --language csharp
./scripts/test.sh --folder 2621_sleep --language scala
./scripts/test.sh --folder 2621_sleep --language php
./scripts/test.sh --folder 2621_sleep --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2621_sleep --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2621_sleep --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2621_sleep --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2621_sleep --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2621_sleep --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2621_sleep --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2621_sleep --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2621_sleep --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2621_sleep --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2621_sleep --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2621_sleep --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2621_sleep --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2621_sleep --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2621_sleep --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2621_sleep
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2621_sleep
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2621_sleep
docker compose -f docker/docker-compose.yml run --rm java java 2621_sleep
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2621_sleep
docker compose -f docker/docker-compose.yml run --rm c c 2621_sleep
docker compose -f docker/docker-compose.yml run --rm go go 2621_sleep
docker compose -f docker/docker-compose.yml run --rm rust rust 2621_sleep
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2621_sleep
docker compose -f docker/docker-compose.yml run --rm swift swift 2621_sleep
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2621_sleep
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2621_sleep
docker compose -f docker/docker-compose.yml run --rm scala scala 2621_sleep
docker compose -f docker/docker-compose.yml run --rm php php 2621_sleep
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2621_sleep` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2621_sleep` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2621_sleep` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2621_sleep` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2621_sleep` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2621_sleep` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2621_sleep` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2621_sleep` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2621_sleep` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2621_sleep` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2621_sleep` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2621_sleep` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2621_sleep` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2621_sleep` |

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
.\scripts\test.ps1 -Folder 2621_sleep -AllLanguages
```

```bash
./scripts/test.sh --folder 2621_sleep --all-languages
```

```zsh
./scripts/test.sh --folder 2621_sleep --all-languages
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
