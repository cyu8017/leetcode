# Test harness for 1255_maximum_score_words_formed_by_letters

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language python
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language javascript
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language typescript
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language java
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language cpp
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language c
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language go
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language rust
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language kotlin
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language swift
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language ruby
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language csharp
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language scala
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language php
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm java java 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm c c 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm go go 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm rust rust 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm swift swift 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm scala scala 1255_maximum_score_words_formed_by_letters
docker compose -f docker/docker-compose.yml run --rm php php 1255_maximum_score_words_formed_by_letters
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1255_maximum_score_words_formed_by_letters` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1255_maximum_score_words_formed_by_letters` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1255_maximum_score_words_formed_by_letters` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1255_maximum_score_words_formed_by_letters` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1255_maximum_score_words_formed_by_letters` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1255_maximum_score_words_formed_by_letters` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1255_maximum_score_words_formed_by_letters` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1255_maximum_score_words_formed_by_letters` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1255_maximum_score_words_formed_by_letters` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1255_maximum_score_words_formed_by_letters` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1255_maximum_score_words_formed_by_letters` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1255_maximum_score_words_formed_by_letters` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1255_maximum_score_words_formed_by_letters` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1255_maximum_score_words_formed_by_letters` |

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
.\scripts\test.ps1 -Folder 1255_maximum_score_words_formed_by_letters -AllLanguages
```

```bash
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --all-languages
```

```zsh
./scripts/test.sh --folder 1255_maximum_score_words_formed_by_letters --all-languages
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
