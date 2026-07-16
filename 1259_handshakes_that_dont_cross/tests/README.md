# Test harness for 1259_handshakes_that_dont_cross

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language python
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language javascript
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language typescript
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language java
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language cpp
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language c
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language go
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language rust
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language kotlin
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language swift
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language ruby
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language csharp
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language scala
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language php
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1259_handshakes_that_dont_cross --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm java java 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm c c 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm go go 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm rust rust 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm swift swift 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm scala scala 1259_handshakes_that_dont_cross
docker compose -f docker/docker-compose.yml run --rm php php 1259_handshakes_that_dont_cross
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1259_handshakes_that_dont_cross` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1259_handshakes_that_dont_cross` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1259_handshakes_that_dont_cross` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1259_handshakes_that_dont_cross` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1259_handshakes_that_dont_cross` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1259_handshakes_that_dont_cross` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1259_handshakes_that_dont_cross` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1259_handshakes_that_dont_cross` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1259_handshakes_that_dont_cross` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1259_handshakes_that_dont_cross` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1259_handshakes_that_dont_cross` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1259_handshakes_that_dont_cross` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1259_handshakes_that_dont_cross` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1259_handshakes_that_dont_cross` |

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
.\scripts\test.ps1 -Folder 1259_handshakes_that_dont_cross -AllLanguages
```

```bash
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --all-languages
```

```zsh
./scripts/test.sh --folder 1259_handshakes_that_dont_cross --all-languages
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
