# Test harness for 0739_daily_temperatures

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0739_daily_temperatures -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0739_daily_temperatures --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0739_daily_temperatures --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0739_daily_temperatures --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0739_daily_temperatures --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0739_daily_temperatures --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0739_daily_temperatures --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0739_daily_temperatures --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0739_daily_temperatures --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0739_daily_temperatures --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0739_daily_temperatures --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0739_daily_temperatures --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0739_daily_temperatures --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0739_daily_temperatures --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0739_daily_temperatures --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0739_daily_temperatures --language python
./scripts/test.sh --folder 0739_daily_temperatures --language javascript
./scripts/test.sh --folder 0739_daily_temperatures --language typescript
./scripts/test.sh --folder 0739_daily_temperatures --language java
./scripts/test.sh --folder 0739_daily_temperatures --language cpp
./scripts/test.sh --folder 0739_daily_temperatures --language c
./scripts/test.sh --folder 0739_daily_temperatures --language go
./scripts/test.sh --folder 0739_daily_temperatures --language rust
./scripts/test.sh --folder 0739_daily_temperatures --language kotlin
./scripts/test.sh --folder 0739_daily_temperatures --language swift
./scripts/test.sh --folder 0739_daily_temperatures --language ruby
./scripts/test.sh --folder 0739_daily_temperatures --language csharp
./scripts/test.sh --folder 0739_daily_temperatures --language scala
./scripts/test.sh --folder 0739_daily_temperatures --language php
./scripts/test.sh --folder 0739_daily_temperatures --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0739_daily_temperatures --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0739_daily_temperatures --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0739_daily_temperatures --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0739_daily_temperatures --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0739_daily_temperatures --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0739_daily_temperatures --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0739_daily_temperatures --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0739_daily_temperatures --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0739_daily_temperatures --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0739_daily_temperatures --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0739_daily_temperatures --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0739_daily_temperatures --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0739_daily_temperatures --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0739_daily_temperatures --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm java java 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm c c 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm go go 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm rust rust 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm swift swift 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm scala scala 0739_daily_temperatures
docker compose -f docker/docker-compose.yml run --rm php php 0739_daily_temperatures
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0739_daily_temperatures` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0739_daily_temperatures` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0739_daily_temperatures` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0739_daily_temperatures` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0739_daily_temperatures` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0739_daily_temperatures` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0739_daily_temperatures` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0739_daily_temperatures` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0739_daily_temperatures` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0739_daily_temperatures` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0739_daily_temperatures` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0739_daily_temperatures` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0739_daily_temperatures` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0739_daily_temperatures` |

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
.\scripts\test.ps1 -Folder 0739_daily_temperatures -AllLanguages
```

```bash
./scripts/test.sh --folder 0739_daily_temperatures --all-languages
```

```zsh
./scripts/test.sh --folder 0739_daily_temperatures --all-languages
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
