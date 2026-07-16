# Test harness for 0720_longest_word_in_dictionary

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language python
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language javascript
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language typescript
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language java
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language cpp
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language c
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language go
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language rust
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language kotlin
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language swift
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language ruby
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language csharp
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language scala
./scripts/test.sh --folder 0720_longest_word_in_dictionary --language php
./scripts/test.sh --folder 0720_longest_word_in_dictionary --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0720_longest_word_in_dictionary --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm java java 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm c c 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm go go 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm rust rust 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm swift swift 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm scala scala 0720_longest_word_in_dictionary
docker compose -f docker/docker-compose.yml run --rm php php 0720_longest_word_in_dictionary
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0720_longest_word_in_dictionary` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0720_longest_word_in_dictionary` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0720_longest_word_in_dictionary` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0720_longest_word_in_dictionary` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0720_longest_word_in_dictionary` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0720_longest_word_in_dictionary` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0720_longest_word_in_dictionary` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0720_longest_word_in_dictionary` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0720_longest_word_in_dictionary` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0720_longest_word_in_dictionary` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0720_longest_word_in_dictionary` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0720_longest_word_in_dictionary` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0720_longest_word_in_dictionary` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0720_longest_word_in_dictionary` |

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
.\scripts\test.ps1 -Folder 0720_longest_word_in_dictionary -AllLanguages
```

```bash
./scripts/test.sh --folder 0720_longest_word_in_dictionary --all-languages
```

```zsh
./scripts/test.sh --folder 0720_longest_word_in_dictionary --all-languages
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
