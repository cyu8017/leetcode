# Test harness for 0648_replace_words

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0648_replace_words -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0648_replace_words --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0648_replace_words --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0648_replace_words --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0648_replace_words --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0648_replace_words --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0648_replace_words --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0648_replace_words --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0648_replace_words --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0648_replace_words --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0648_replace_words --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0648_replace_words --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0648_replace_words --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0648_replace_words --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0648_replace_words --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0648_replace_words --language python
./scripts/test.sh --folder 0648_replace_words --language javascript
./scripts/test.sh --folder 0648_replace_words --language typescript
./scripts/test.sh --folder 0648_replace_words --language java
./scripts/test.sh --folder 0648_replace_words --language cpp
./scripts/test.sh --folder 0648_replace_words --language c
./scripts/test.sh --folder 0648_replace_words --language go
./scripts/test.sh --folder 0648_replace_words --language rust
./scripts/test.sh --folder 0648_replace_words --language kotlin
./scripts/test.sh --folder 0648_replace_words --language swift
./scripts/test.sh --folder 0648_replace_words --language ruby
./scripts/test.sh --folder 0648_replace_words --language csharp
./scripts/test.sh --folder 0648_replace_words --language scala
./scripts/test.sh --folder 0648_replace_words --language php
./scripts/test.sh --folder 0648_replace_words --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0648_replace_words --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0648_replace_words --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0648_replace_words --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0648_replace_words --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0648_replace_words --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0648_replace_words --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0648_replace_words --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0648_replace_words --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0648_replace_words --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0648_replace_words --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0648_replace_words --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0648_replace_words --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0648_replace_words --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0648_replace_words --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm java java 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm c c 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm go go 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm rust rust 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm swift swift 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm scala scala 0648_replace_words
docker compose -f docker/docker-compose.yml run --rm php php 0648_replace_words
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0648_replace_words` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0648_replace_words` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0648_replace_words` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0648_replace_words` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0648_replace_words` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0648_replace_words` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0648_replace_words` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0648_replace_words` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0648_replace_words` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0648_replace_words` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0648_replace_words` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0648_replace_words` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0648_replace_words` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0648_replace_words` |

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
.\scripts\test.ps1 -Folder 0648_replace_words -AllLanguages
```

```bash
./scripts/test.sh --folder 0648_replace_words --all-languages
```

```zsh
./scripts/test.sh --folder 0648_replace_words --all-languages
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
