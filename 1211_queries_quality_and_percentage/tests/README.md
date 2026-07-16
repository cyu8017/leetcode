# Test harness for 1211_queries_quality_and_percentage

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language python
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language javascript
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language typescript
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language java
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language cpp
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language c
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language go
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language rust
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language kotlin
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language swift
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language ruby
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language csharp
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language scala
./scripts/test.sh --folder 1211_queries_quality_and_percentage --language php
./scripts/test.sh --folder 1211_queries_quality_and_percentage --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1211_queries_quality_and_percentage --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm java java 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm c c 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm go go 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm rust rust 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm swift swift 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm scala scala 1211_queries_quality_and_percentage
docker compose -f docker/docker-compose.yml run --rm php php 1211_queries_quality_and_percentage
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1211_queries_quality_and_percentage` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1211_queries_quality_and_percentage` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1211_queries_quality_and_percentage` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1211_queries_quality_and_percentage` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1211_queries_quality_and_percentage` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1211_queries_quality_and_percentage` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1211_queries_quality_and_percentage` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1211_queries_quality_and_percentage` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1211_queries_quality_and_percentage` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1211_queries_quality_and_percentage` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1211_queries_quality_and_percentage` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1211_queries_quality_and_percentage` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1211_queries_quality_and_percentage` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1211_queries_quality_and_percentage` |

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
.\scripts\test.ps1 -Folder 1211_queries_quality_and_percentage -AllLanguages
```

```bash
./scripts/test.sh --folder 1211_queries_quality_and_percentage --all-languages
```

```zsh
./scripts/test.sh --folder 1211_queries_quality_and_percentage --all-languages
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
