# Test harness for 1894_find_the_student_that_will_replace_the_chalk

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language python
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language javascript
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language typescript
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language java
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language cpp
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language c
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language go
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language rust
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language kotlin
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language swift
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language ruby
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language csharp
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language scala
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language php
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm java java 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm c c 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm go go 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm rust rust 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm swift swift 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm scala scala 1894_find_the_student_that_will_replace_the_chalk
docker compose -f docker/docker-compose.yml run --rm php php 1894_find_the_student_that_will_replace_the_chalk
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1894_find_the_student_that_will_replace_the_chalk` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1894_find_the_student_that_will_replace_the_chalk` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1894_find_the_student_that_will_replace_the_chalk` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1894_find_the_student_that_will_replace_the_chalk` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1894_find_the_student_that_will_replace_the_chalk` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1894_find_the_student_that_will_replace_the_chalk` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1894_find_the_student_that_will_replace_the_chalk` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1894_find_the_student_that_will_replace_the_chalk` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1894_find_the_student_that_will_replace_the_chalk` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1894_find_the_student_that_will_replace_the_chalk` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1894_find_the_student_that_will_replace_the_chalk` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1894_find_the_student_that_will_replace_the_chalk` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1894_find_the_student_that_will_replace_the_chalk` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1894_find_the_student_that_will_replace_the_chalk` |

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
.\scripts\test.ps1 -Folder 1894_find_the_student_that_will_replace_the_chalk -AllLanguages
```

```bash
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --all-languages
```

```zsh
./scripts/test.sh --folder 1894_find_the_student_that_will_replace_the_chalk --all-languages
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
