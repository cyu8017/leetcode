# Test harness for 1033_moving_stones_until_consecutive

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language python
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language javascript
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language typescript
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language java
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language cpp
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language c
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language go
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language rust
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language kotlin
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language swift
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language ruby
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language csharp
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language scala
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language php
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1033_moving_stones_until_consecutive --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm java java 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm c c 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm go go 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm rust rust 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm swift swift 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm scala scala 1033_moving_stones_until_consecutive
docker compose -f docker/docker-compose.yml run --rm php php 1033_moving_stones_until_consecutive
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1033_moving_stones_until_consecutive` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1033_moving_stones_until_consecutive` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1033_moving_stones_until_consecutive` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1033_moving_stones_until_consecutive` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1033_moving_stones_until_consecutive` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1033_moving_stones_until_consecutive` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1033_moving_stones_until_consecutive` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1033_moving_stones_until_consecutive` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1033_moving_stones_until_consecutive` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1033_moving_stones_until_consecutive` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1033_moving_stones_until_consecutive` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1033_moving_stones_until_consecutive` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1033_moving_stones_until_consecutive` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1033_moving_stones_until_consecutive` |

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
.\scripts\test.ps1 -Folder 1033_moving_stones_until_consecutive -AllLanguages
```

```bash
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --all-languages
```

```zsh
./scripts/test.sh --folder 1033_moving_stones_until_consecutive --all-languages
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
