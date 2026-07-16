# Test harness for 2140_solving_questions_with_brainpower

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language python
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language javascript
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language typescript
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language java
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language cpp
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language c
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language go
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language rust
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language kotlin
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language swift
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language ruby
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language csharp
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language scala
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language php
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2140_solving_questions_with_brainpower --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm java java 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm c c 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm go go 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm rust rust 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm swift swift 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm scala scala 2140_solving_questions_with_brainpower
docker compose -f docker/docker-compose.yml run --rm php php 2140_solving_questions_with_brainpower
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2140_solving_questions_with_brainpower` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2140_solving_questions_with_brainpower` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2140_solving_questions_with_brainpower` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2140_solving_questions_with_brainpower` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2140_solving_questions_with_brainpower` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2140_solving_questions_with_brainpower` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2140_solving_questions_with_brainpower` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2140_solving_questions_with_brainpower` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2140_solving_questions_with_brainpower` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2140_solving_questions_with_brainpower` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2140_solving_questions_with_brainpower` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2140_solving_questions_with_brainpower` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2140_solving_questions_with_brainpower` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2140_solving_questions_with_brainpower` |

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
.\scripts\test.ps1 -Folder 2140_solving_questions_with_brainpower -AllLanguages
```

```bash
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --all-languages
```

```zsh
./scripts/test.sh --folder 2140_solving_questions_with_brainpower --all-languages
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
