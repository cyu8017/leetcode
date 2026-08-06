# Test harness for 4012_count_of_unfinished_tasks_after_each_shift

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language python
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language javascript
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language typescript
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language java
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language cpp
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language c
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language go
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language rust
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language kotlin
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language swift
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language ruby
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language csharp
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language scala
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language php
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm javascript javascript 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm typescript typescript 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm java java 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm cpp cpp 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm c c 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm go go 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm rust rust 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm swift swift 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm ruby ruby 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm csharp csharp 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm scala scala 4012_count_of_unfinished_tasks_after_each_shift
docker compose -f docker/docker-compose.yml run --rm php php 4012_count_of_unfinished_tasks_after_each_shift
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 4012_count_of_unfinished_tasks_after_each_shift` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 4012_count_of_unfinished_tasks_after_each_shift` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 4012_count_of_unfinished_tasks_after_each_shift` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 4012_count_of_unfinished_tasks_after_each_shift` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 4012_count_of_unfinished_tasks_after_each_shift` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 4012_count_of_unfinished_tasks_after_each_shift` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 4012_count_of_unfinished_tasks_after_each_shift` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 4012_count_of_unfinished_tasks_after_each_shift` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 4012_count_of_unfinished_tasks_after_each_shift` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 4012_count_of_unfinished_tasks_after_each_shift` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 4012_count_of_unfinished_tasks_after_each_shift` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 4012_count_of_unfinished_tasks_after_each_shift` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 4012_count_of_unfinished_tasks_after_each_shift` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 4012_count_of_unfinished_tasks_after_each_shift` |

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
.\scripts\test.ps1 -Folder 4012_count_of_unfinished_tasks_after_each_shift -AllLanguages
```

```bash
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --all-languages
```

```zsh
./scripts/test.sh --folder 4012_count_of_unfinished_tasks_after_each_shift --all-languages
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
