# Test harness for 0211_design_add_and_search_words_data_structure

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language python
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language javascript
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language typescript
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language java
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language cpp
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language c
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language go
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language rust
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language kotlin
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language swift
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language ruby
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language csharp
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language scala
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language php
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm java java 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm c c 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm go go 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm rust rust 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm swift swift 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm scala scala 0211_design_add_and_search_words_data_structure
docker compose -f docker/docker-compose.yml run --rm php php 0211_design_add_and_search_words_data_structure
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0211_design_add_and_search_words_data_structure` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0211_design_add_and_search_words_data_structure` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0211_design_add_and_search_words_data_structure` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0211_design_add_and_search_words_data_structure` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0211_design_add_and_search_words_data_structure` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0211_design_add_and_search_words_data_structure` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0211_design_add_and_search_words_data_structure` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0211_design_add_and_search_words_data_structure` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0211_design_add_and_search_words_data_structure` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0211_design_add_and_search_words_data_structure` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0211_design_add_and_search_words_data_structure` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0211_design_add_and_search_words_data_structure` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0211_design_add_and_search_words_data_structure` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0211_design_add_and_search_words_data_structure` |

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
.\scripts\test.ps1 -Folder 0211_design_add_and_search_words_data_structure -AllLanguages
```

```bash
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --all-languages
```

```zsh
./scripts/test.sh --folder 0211_design_add_and_search_words_data_structure --all-languages
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
