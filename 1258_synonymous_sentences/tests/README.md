# Test harness for 1258_synonymous_sentences

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1258_synonymous_sentences -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1258_synonymous_sentences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1258_synonymous_sentences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1258_synonymous_sentences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1258_synonymous_sentences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1258_synonymous_sentences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1258_synonymous_sentences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1258_synonymous_sentences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1258_synonymous_sentences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1258_synonymous_sentences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1258_synonymous_sentences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1258_synonymous_sentences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1258_synonymous_sentences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1258_synonymous_sentences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1258_synonymous_sentences --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1258_synonymous_sentences --language python
./scripts/test.sh --folder 1258_synonymous_sentences --language javascript
./scripts/test.sh --folder 1258_synonymous_sentences --language typescript
./scripts/test.sh --folder 1258_synonymous_sentences --language java
./scripts/test.sh --folder 1258_synonymous_sentences --language cpp
./scripts/test.sh --folder 1258_synonymous_sentences --language c
./scripts/test.sh --folder 1258_synonymous_sentences --language go
./scripts/test.sh --folder 1258_synonymous_sentences --language rust
./scripts/test.sh --folder 1258_synonymous_sentences --language kotlin
./scripts/test.sh --folder 1258_synonymous_sentences --language swift
./scripts/test.sh --folder 1258_synonymous_sentences --language ruby
./scripts/test.sh --folder 1258_synonymous_sentences --language csharp
./scripts/test.sh --folder 1258_synonymous_sentences --language scala
./scripts/test.sh --folder 1258_synonymous_sentences --language php
./scripts/test.sh --folder 1258_synonymous_sentences --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1258_synonymous_sentences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1258_synonymous_sentences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1258_synonymous_sentences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1258_synonymous_sentences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1258_synonymous_sentences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1258_synonymous_sentences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1258_synonymous_sentences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1258_synonymous_sentences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1258_synonymous_sentences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1258_synonymous_sentences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1258_synonymous_sentences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1258_synonymous_sentences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1258_synonymous_sentences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1258_synonymous_sentences --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm java java 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm c c 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm go go 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm rust rust 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm swift swift 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm scala scala 1258_synonymous_sentences
docker compose -f docker/docker-compose.yml run --rm php php 1258_synonymous_sentences
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1258_synonymous_sentences` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1258_synonymous_sentences` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1258_synonymous_sentences` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1258_synonymous_sentences` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1258_synonymous_sentences` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1258_synonymous_sentences` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1258_synonymous_sentences` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1258_synonymous_sentences` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1258_synonymous_sentences` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1258_synonymous_sentences` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1258_synonymous_sentences` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1258_synonymous_sentences` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1258_synonymous_sentences` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1258_synonymous_sentences` |

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
.\scripts\test.ps1 -Folder 1258_synonymous_sentences -AllLanguages
```

```bash
./scripts/test.sh --folder 1258_synonymous_sentences --all-languages
```

```zsh
./scripts/test.sh --folder 1258_synonymous_sentences --all-languages
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
