# Test harness for 1280_students_and_examinations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1280_students_and_examinations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1280_students_and_examinations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1280_students_and_examinations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1280_students_and_examinations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1280_students_and_examinations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1280_students_and_examinations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1280_students_and_examinations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1280_students_and_examinations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1280_students_and_examinations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1280_students_and_examinations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1280_students_and_examinations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1280_students_and_examinations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1280_students_and_examinations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1280_students_and_examinations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1280_students_and_examinations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1280_students_and_examinations --language python
./scripts/test.sh --folder 1280_students_and_examinations --language javascript
./scripts/test.sh --folder 1280_students_and_examinations --language typescript
./scripts/test.sh --folder 1280_students_and_examinations --language java
./scripts/test.sh --folder 1280_students_and_examinations --language cpp
./scripts/test.sh --folder 1280_students_and_examinations --language c
./scripts/test.sh --folder 1280_students_and_examinations --language go
./scripts/test.sh --folder 1280_students_and_examinations --language rust
./scripts/test.sh --folder 1280_students_and_examinations --language kotlin
./scripts/test.sh --folder 1280_students_and_examinations --language swift
./scripts/test.sh --folder 1280_students_and_examinations --language ruby
./scripts/test.sh --folder 1280_students_and_examinations --language csharp
./scripts/test.sh --folder 1280_students_and_examinations --language scala
./scripts/test.sh --folder 1280_students_and_examinations --language php
./scripts/test.sh --folder 1280_students_and_examinations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1280_students_and_examinations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1280_students_and_examinations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1280_students_and_examinations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1280_students_and_examinations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1280_students_and_examinations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1280_students_and_examinations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1280_students_and_examinations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1280_students_and_examinations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1280_students_and_examinations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1280_students_and_examinations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1280_students_and_examinations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1280_students_and_examinations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1280_students_and_examinations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1280_students_and_examinations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm java java 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm c c 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm go go 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm rust rust 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm swift swift 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm scala scala 1280_students_and_examinations
docker compose -f docker/docker-compose.yml run --rm php php 1280_students_and_examinations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1280_students_and_examinations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1280_students_and_examinations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1280_students_and_examinations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1280_students_and_examinations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1280_students_and_examinations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1280_students_and_examinations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1280_students_and_examinations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1280_students_and_examinations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1280_students_and_examinations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1280_students_and_examinations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1280_students_and_examinations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1280_students_and_examinations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1280_students_and_examinations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1280_students_and_examinations` |

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
.\scripts\test.ps1 -Folder 1280_students_and_examinations -AllLanguages
```

```bash
./scripts/test.sh --folder 1280_students_and_examinations --all-languages
```

```zsh
./scripts/test.sh --folder 1280_students_and_examinations --all-languages
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
