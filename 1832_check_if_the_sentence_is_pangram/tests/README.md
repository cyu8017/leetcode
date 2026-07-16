# Test harness for 1832_check_if_the_sentence_is_pangram

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language python
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language javascript
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language typescript
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language java
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language cpp
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language c
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language go
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language rust
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language kotlin
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language swift
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language ruby
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language csharp
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language scala
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language php
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm java java 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm c c 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm go go 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm rust rust 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm swift swift 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm scala scala 1832_check_if_the_sentence_is_pangram
docker compose -f docker/docker-compose.yml run --rm php php 1832_check_if_the_sentence_is_pangram
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1832_check_if_the_sentence_is_pangram` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1832_check_if_the_sentence_is_pangram` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1832_check_if_the_sentence_is_pangram` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1832_check_if_the_sentence_is_pangram` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1832_check_if_the_sentence_is_pangram` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1832_check_if_the_sentence_is_pangram` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1832_check_if_the_sentence_is_pangram` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1832_check_if_the_sentence_is_pangram` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1832_check_if_the_sentence_is_pangram` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1832_check_if_the_sentence_is_pangram` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1832_check_if_the_sentence_is_pangram` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1832_check_if_the_sentence_is_pangram` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1832_check_if_the_sentence_is_pangram` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1832_check_if_the_sentence_is_pangram` |

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
.\scripts\test.ps1 -Folder 1832_check_if_the_sentence_is_pangram -AllLanguages
```

```bash
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --all-languages
```

```zsh
./scripts/test.sh --folder 1832_check_if_the_sentence_is_pangram --all-languages
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
