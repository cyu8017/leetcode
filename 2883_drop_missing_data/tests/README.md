# Test harness for 2883_drop_missing_data

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2883_drop_missing_data -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2883_drop_missing_data --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2883_drop_missing_data --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2883_drop_missing_data --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2883_drop_missing_data --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2883_drop_missing_data --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2883_drop_missing_data --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2883_drop_missing_data --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2883_drop_missing_data --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2883_drop_missing_data --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2883_drop_missing_data --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2883_drop_missing_data --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2883_drop_missing_data --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2883_drop_missing_data --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2883_drop_missing_data --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2883_drop_missing_data --language python
./scripts/test.sh --folder 2883_drop_missing_data --language javascript
./scripts/test.sh --folder 2883_drop_missing_data --language typescript
./scripts/test.sh --folder 2883_drop_missing_data --language java
./scripts/test.sh --folder 2883_drop_missing_data --language cpp
./scripts/test.sh --folder 2883_drop_missing_data --language c
./scripts/test.sh --folder 2883_drop_missing_data --language go
./scripts/test.sh --folder 2883_drop_missing_data --language rust
./scripts/test.sh --folder 2883_drop_missing_data --language kotlin
./scripts/test.sh --folder 2883_drop_missing_data --language swift
./scripts/test.sh --folder 2883_drop_missing_data --language ruby
./scripts/test.sh --folder 2883_drop_missing_data --language csharp
./scripts/test.sh --folder 2883_drop_missing_data --language scala
./scripts/test.sh --folder 2883_drop_missing_data --language php
./scripts/test.sh --folder 2883_drop_missing_data --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2883_drop_missing_data --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2883_drop_missing_data --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2883_drop_missing_data --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2883_drop_missing_data --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2883_drop_missing_data --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2883_drop_missing_data --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2883_drop_missing_data --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2883_drop_missing_data --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2883_drop_missing_data --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2883_drop_missing_data --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2883_drop_missing_data --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2883_drop_missing_data --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2883_drop_missing_data --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2883_drop_missing_data --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm java java 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm c c 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm go go 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm rust rust 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm swift swift 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm scala scala 2883_drop_missing_data
docker compose -f docker/docker-compose.yml run --rm php php 2883_drop_missing_data
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2883_drop_missing_data` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2883_drop_missing_data` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2883_drop_missing_data` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2883_drop_missing_data` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2883_drop_missing_data` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2883_drop_missing_data` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2883_drop_missing_data` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2883_drop_missing_data` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2883_drop_missing_data` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2883_drop_missing_data` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2883_drop_missing_data` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2883_drop_missing_data` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2883_drop_missing_data` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2883_drop_missing_data` |

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
.\scripts\test.ps1 -Folder 2883_drop_missing_data -AllLanguages
```

```bash
./scripts/test.sh --folder 2883_drop_missing_data --all-languages
```

```zsh
./scripts/test.sh --folder 2883_drop_missing_data --all-languages
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
