# Test harness for 2114_maximum_number_of_words_found_in_sentences

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language python
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language javascript
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language typescript
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language java
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language cpp
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language c
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language go
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language rust
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language kotlin
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language swift
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language ruby
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language csharp
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language scala
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language php
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm java java 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm c c 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm go go 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm rust rust 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm swift swift 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm scala scala 2114_maximum_number_of_words_found_in_sentences
docker compose -f docker/docker-compose.yml run --rm php php 2114_maximum_number_of_words_found_in_sentences
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2114_maximum_number_of_words_found_in_sentences` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2114_maximum_number_of_words_found_in_sentences` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2114_maximum_number_of_words_found_in_sentences` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2114_maximum_number_of_words_found_in_sentences` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2114_maximum_number_of_words_found_in_sentences` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2114_maximum_number_of_words_found_in_sentences` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2114_maximum_number_of_words_found_in_sentences` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2114_maximum_number_of_words_found_in_sentences` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2114_maximum_number_of_words_found_in_sentences` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2114_maximum_number_of_words_found_in_sentences` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2114_maximum_number_of_words_found_in_sentences` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2114_maximum_number_of_words_found_in_sentences` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2114_maximum_number_of_words_found_in_sentences` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2114_maximum_number_of_words_found_in_sentences` |

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
.\scripts\test.ps1 -Folder 2114_maximum_number_of_words_found_in_sentences -AllLanguages
```

```bash
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --all-languages
```

```zsh
./scripts/test.sh --folder 2114_maximum_number_of_words_found_in_sentences --all-languages
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
