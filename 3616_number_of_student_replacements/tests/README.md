# Test harness for 3616_number_of_student_replacements

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3616_number_of_student_replacements --language python
./scripts/test.sh --folder 3616_number_of_student_replacements --language javascript
./scripts/test.sh --folder 3616_number_of_student_replacements --language typescript
./scripts/test.sh --folder 3616_number_of_student_replacements --language java
./scripts/test.sh --folder 3616_number_of_student_replacements --language cpp
./scripts/test.sh --folder 3616_number_of_student_replacements --language c
./scripts/test.sh --folder 3616_number_of_student_replacements --language go
./scripts/test.sh --folder 3616_number_of_student_replacements --language rust
./scripts/test.sh --folder 3616_number_of_student_replacements --language kotlin
./scripts/test.sh --folder 3616_number_of_student_replacements --language swift
./scripts/test.sh --folder 3616_number_of_student_replacements --language ruby
./scripts/test.sh --folder 3616_number_of_student_replacements --language csharp
./scripts/test.sh --folder 3616_number_of_student_replacements --language scala
./scripts/test.sh --folder 3616_number_of_student_replacements --language php
./scripts/test.sh --folder 3616_number_of_student_replacements --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3616_number_of_student_replacements --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm java java 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm c c 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm go go 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm rust rust 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm swift swift 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm scala scala 3616_number_of_student_replacements
docker compose -f docker/docker-compose.yml run --rm php php 3616_number_of_student_replacements
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3616_number_of_student_replacements` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3616_number_of_student_replacements` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3616_number_of_student_replacements` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3616_number_of_student_replacements` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3616_number_of_student_replacements` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3616_number_of_student_replacements` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3616_number_of_student_replacements` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3616_number_of_student_replacements` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3616_number_of_student_replacements` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3616_number_of_student_replacements` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3616_number_of_student_replacements` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3616_number_of_student_replacements` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3616_number_of_student_replacements` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3616_number_of_student_replacements` |

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
.\scripts\test.ps1 -Folder 3616_number_of_student_replacements -AllLanguages
```

```bash
./scripts/test.sh --folder 3616_number_of_student_replacements --all-languages
```

```zsh
./scripts/test.sh --folder 3616_number_of_student_replacements --all-languages
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
