# Test harness for 2545_sort_the_students_by_their_kth_score

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language python
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language javascript
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language typescript
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language java
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language cpp
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language c
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language go
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language rust
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language kotlin
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language swift
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language ruby
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language csharp
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language scala
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language php
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm java java 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm c c 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm go go 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm rust rust 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm swift swift 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm scala scala 2545_sort_the_students_by_their_kth_score
docker compose -f docker/docker-compose.yml run --rm php php 2545_sort_the_students_by_their_kth_score
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2545_sort_the_students_by_their_kth_score` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2545_sort_the_students_by_their_kth_score` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2545_sort_the_students_by_their_kth_score` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2545_sort_the_students_by_their_kth_score` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2545_sort_the_students_by_their_kth_score` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2545_sort_the_students_by_their_kth_score` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2545_sort_the_students_by_their_kth_score` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2545_sort_the_students_by_their_kth_score` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2545_sort_the_students_by_their_kth_score` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2545_sort_the_students_by_their_kth_score` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2545_sort_the_students_by_their_kth_score` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2545_sort_the_students_by_their_kth_score` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2545_sort_the_students_by_their_kth_score` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2545_sort_the_students_by_their_kth_score` |

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
.\scripts\test.ps1 -Folder 2545_sort_the_students_by_their_kth_score -AllLanguages
```

```bash
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --all-languages
```

```zsh
./scripts/test.sh --folder 2545_sort_the_students_by_their_kth_score --all-languages
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
