# Test harness for 2085_count_common_words_with_one_occurrence

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language python
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language javascript
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language typescript
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language java
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language cpp
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language c
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language go
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language rust
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language kotlin
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language swift
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language ruby
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language csharp
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language scala
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language php
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm java java 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm c c 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm go go 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm rust rust 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm swift swift 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm scala scala 2085_count_common_words_with_one_occurrence
docker compose -f docker/docker-compose.yml run --rm php php 2085_count_common_words_with_one_occurrence
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2085_count_common_words_with_one_occurrence` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2085_count_common_words_with_one_occurrence` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2085_count_common_words_with_one_occurrence` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2085_count_common_words_with_one_occurrence` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2085_count_common_words_with_one_occurrence` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2085_count_common_words_with_one_occurrence` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2085_count_common_words_with_one_occurrence` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2085_count_common_words_with_one_occurrence` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2085_count_common_words_with_one_occurrence` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2085_count_common_words_with_one_occurrence` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2085_count_common_words_with_one_occurrence` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2085_count_common_words_with_one_occurrence` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2085_count_common_words_with_one_occurrence` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2085_count_common_words_with_one_occurrence` |

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
.\scripts\test.ps1 -Folder 2085_count_common_words_with_one_occurrence -AllLanguages
```

```bash
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --all-languages
```

```zsh
./scripts/test.sh --folder 2085_count_common_words_with_one_occurrence --all-languages
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
