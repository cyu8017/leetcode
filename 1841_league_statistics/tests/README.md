# Test harness for 1841_league_statistics

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1841_league_statistics -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1841_league_statistics --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1841_league_statistics --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1841_league_statistics --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1841_league_statistics --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1841_league_statistics --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1841_league_statistics --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1841_league_statistics --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1841_league_statistics --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1841_league_statistics --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1841_league_statistics --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1841_league_statistics --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1841_league_statistics --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1841_league_statistics --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1841_league_statistics --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1841_league_statistics --language python
./scripts/test.sh --folder 1841_league_statistics --language javascript
./scripts/test.sh --folder 1841_league_statistics --language typescript
./scripts/test.sh --folder 1841_league_statistics --language java
./scripts/test.sh --folder 1841_league_statistics --language cpp
./scripts/test.sh --folder 1841_league_statistics --language c
./scripts/test.sh --folder 1841_league_statistics --language go
./scripts/test.sh --folder 1841_league_statistics --language rust
./scripts/test.sh --folder 1841_league_statistics --language kotlin
./scripts/test.sh --folder 1841_league_statistics --language swift
./scripts/test.sh --folder 1841_league_statistics --language ruby
./scripts/test.sh --folder 1841_league_statistics --language csharp
./scripts/test.sh --folder 1841_league_statistics --language scala
./scripts/test.sh --folder 1841_league_statistics --language php
./scripts/test.sh --folder 1841_league_statistics --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1841_league_statistics --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1841_league_statistics --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1841_league_statistics --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1841_league_statistics --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1841_league_statistics --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1841_league_statistics --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1841_league_statistics --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1841_league_statistics --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1841_league_statistics --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1841_league_statistics --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1841_league_statistics --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1841_league_statistics --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1841_league_statistics --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1841_league_statistics --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm java java 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm c c 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm go go 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm rust rust 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm swift swift 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm scala scala 1841_league_statistics
docker compose -f docker/docker-compose.yml run --rm php php 1841_league_statistics
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1841_league_statistics` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1841_league_statistics` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1841_league_statistics` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1841_league_statistics` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1841_league_statistics` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1841_league_statistics` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1841_league_statistics` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1841_league_statistics` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1841_league_statistics` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1841_league_statistics` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1841_league_statistics` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1841_league_statistics` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1841_league_statistics` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1841_league_statistics` |

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
.\scripts\test.ps1 -Folder 1841_league_statistics -AllLanguages
```

```bash
./scripts/test.sh --folder 1841_league_statistics --all-languages
```

```zsh
./scripts/test.sh --folder 1841_league_statistics --all-languages
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
