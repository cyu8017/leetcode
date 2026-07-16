# Test harness for 2721_execute_asynchronous_functions_in_parallel

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language python
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language javascript
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language typescript
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language java
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language cpp
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language c
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language go
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language rust
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language kotlin
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language swift
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language ruby
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language csharp
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language scala
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language php
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm java java 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm c c 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm go go 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm rust rust 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm swift swift 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm scala scala 2721_execute_asynchronous_functions_in_parallel
docker compose -f docker/docker-compose.yml run --rm php php 2721_execute_asynchronous_functions_in_parallel
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2721_execute_asynchronous_functions_in_parallel` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2721_execute_asynchronous_functions_in_parallel` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2721_execute_asynchronous_functions_in_parallel` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2721_execute_asynchronous_functions_in_parallel` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2721_execute_asynchronous_functions_in_parallel` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2721_execute_asynchronous_functions_in_parallel` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2721_execute_asynchronous_functions_in_parallel` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2721_execute_asynchronous_functions_in_parallel` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2721_execute_asynchronous_functions_in_parallel` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2721_execute_asynchronous_functions_in_parallel` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2721_execute_asynchronous_functions_in_parallel` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2721_execute_asynchronous_functions_in_parallel` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2721_execute_asynchronous_functions_in_parallel` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2721_execute_asynchronous_functions_in_parallel` |

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
.\scripts\test.ps1 -Folder 2721_execute_asynchronous_functions_in_parallel -AllLanguages
```

```bash
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --all-languages
```

```zsh
./scripts/test.sh --folder 2721_execute_asynchronous_functions_in_parallel --all-languages
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
