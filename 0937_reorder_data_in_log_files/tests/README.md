# Test harness for 0937_reorder_data_in_log_files

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language python
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language javascript
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language typescript
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language java
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language cpp
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language c
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language go
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language rust
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language kotlin
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language swift
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language ruby
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language csharp
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language scala
./scripts/test.sh --folder 0937_reorder_data_in_log_files --language php
./scripts/test.sh --folder 0937_reorder_data_in_log_files --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0937_reorder_data_in_log_files --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm java java 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm c c 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm go go 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm rust rust 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm swift swift 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm scala scala 0937_reorder_data_in_log_files
docker compose -f docker/docker-compose.yml run --rm php php 0937_reorder_data_in_log_files
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0937_reorder_data_in_log_files` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0937_reorder_data_in_log_files` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0937_reorder_data_in_log_files` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0937_reorder_data_in_log_files` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0937_reorder_data_in_log_files` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0937_reorder_data_in_log_files` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0937_reorder_data_in_log_files` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0937_reorder_data_in_log_files` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0937_reorder_data_in_log_files` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0937_reorder_data_in_log_files` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0937_reorder_data_in_log_files` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0937_reorder_data_in_log_files` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0937_reorder_data_in_log_files` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0937_reorder_data_in_log_files` |

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
.\scripts\test.ps1 -Folder 0937_reorder_data_in_log_files -AllLanguages
```

```bash
./scripts/test.sh --folder 0937_reorder_data_in_log_files --all-languages
```

```zsh
./scripts/test.sh --folder 0937_reorder_data_in_log_files --all-languages
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
