# Test harness for 3758_convert_number_words_to_digits

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language python
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language javascript
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language typescript
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language java
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language cpp
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language c
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language go
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language rust
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language kotlin
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language swift
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language ruby
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language csharp
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language scala
./scripts/test.sh --folder 3758_convert_number_words_to_digits --language php
./scripts/test.sh --folder 3758_convert_number_words_to_digits --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3758_convert_number_words_to_digits --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm java java 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm c c 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm go go 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm rust rust 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm swift swift 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm scala scala 3758_convert_number_words_to_digits
docker compose -f docker/docker-compose.yml run --rm php php 3758_convert_number_words_to_digits
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3758_convert_number_words_to_digits` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3758_convert_number_words_to_digits` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3758_convert_number_words_to_digits` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3758_convert_number_words_to_digits` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3758_convert_number_words_to_digits` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3758_convert_number_words_to_digits` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3758_convert_number_words_to_digits` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3758_convert_number_words_to_digits` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3758_convert_number_words_to_digits` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3758_convert_number_words_to_digits` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3758_convert_number_words_to_digits` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3758_convert_number_words_to_digits` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3758_convert_number_words_to_digits` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3758_convert_number_words_to_digits` |

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
.\scripts\test.ps1 -Folder 3758_convert_number_words_to_digits -AllLanguages
```

```bash
./scripts/test.sh --folder 3758_convert_number_words_to_digits --all-languages
```

```zsh
./scripts/test.sh --folder 3758_convert_number_words_to_digits --all-languages
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
