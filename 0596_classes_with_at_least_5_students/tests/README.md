# Test harness for 0596_classes_with_at_least_5_students

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language python
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language javascript
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language typescript
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language java
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language cpp
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language c
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language go
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language rust
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language kotlin
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language swift
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language ruby
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language csharp
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language scala
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language php
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0596_classes_with_at_least_5_students --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm java java 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm c c 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm go go 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm rust rust 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm swift swift 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm scala scala 0596_classes_with_at_least_5_students
docker compose -f docker/docker-compose.yml run --rm php php 0596_classes_with_at_least_5_students
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0596_classes_with_at_least_5_students` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0596_classes_with_at_least_5_students` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0596_classes_with_at_least_5_students` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0596_classes_with_at_least_5_students` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0596_classes_with_at_least_5_students` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0596_classes_with_at_least_5_students` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0596_classes_with_at_least_5_students` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0596_classes_with_at_least_5_students` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0596_classes_with_at_least_5_students` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0596_classes_with_at_least_5_students` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0596_classes_with_at_least_5_students` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0596_classes_with_at_least_5_students` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0596_classes_with_at_least_5_students` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0596_classes_with_at_least_5_students` |

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
.\scripts\test.ps1 -Folder 0596_classes_with_at_least_5_students -AllLanguages
```

```bash
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --all-languages
```

```zsh
./scripts/test.sh --folder 0596_classes_with_at_least_5_students --all-languages
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
