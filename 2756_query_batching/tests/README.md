# Test harness for 2756_query_batching

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2756_query_batching -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2756_query_batching --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2756_query_batching --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2756_query_batching --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2756_query_batching --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2756_query_batching --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2756_query_batching --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2756_query_batching --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2756_query_batching --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2756_query_batching --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2756_query_batching --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2756_query_batching --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2756_query_batching --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2756_query_batching --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2756_query_batching --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2756_query_batching --language python
./scripts/test.sh --folder 2756_query_batching --language javascript
./scripts/test.sh --folder 2756_query_batching --language typescript
./scripts/test.sh --folder 2756_query_batching --language java
./scripts/test.sh --folder 2756_query_batching --language cpp
./scripts/test.sh --folder 2756_query_batching --language c
./scripts/test.sh --folder 2756_query_batching --language go
./scripts/test.sh --folder 2756_query_batching --language rust
./scripts/test.sh --folder 2756_query_batching --language kotlin
./scripts/test.sh --folder 2756_query_batching --language swift
./scripts/test.sh --folder 2756_query_batching --language ruby
./scripts/test.sh --folder 2756_query_batching --language csharp
./scripts/test.sh --folder 2756_query_batching --language scala
./scripts/test.sh --folder 2756_query_batching --language php
./scripts/test.sh --folder 2756_query_batching --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2756_query_batching --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2756_query_batching --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2756_query_batching --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2756_query_batching --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2756_query_batching --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2756_query_batching --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2756_query_batching --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2756_query_batching --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2756_query_batching --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2756_query_batching --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2756_query_batching --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2756_query_batching --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2756_query_batching --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2756_query_batching --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm java java 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm c c 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm go go 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm rust rust 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm swift swift 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm scala scala 2756_query_batching
docker compose -f docker/docker-compose.yml run --rm php php 2756_query_batching
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2756_query_batching` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2756_query_batching` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2756_query_batching` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2756_query_batching` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2756_query_batching` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2756_query_batching` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2756_query_batching` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2756_query_batching` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2756_query_batching` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2756_query_batching` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2756_query_batching` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2756_query_batching` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2756_query_batching` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2756_query_batching` |

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
.\scripts\test.ps1 -Folder 2756_query_batching -AllLanguages
```

```bash
./scripts/test.sh --folder 2756_query_batching --all-languages
```

```zsh
./scripts/test.sh --folder 2756_query_batching --all-languages
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
