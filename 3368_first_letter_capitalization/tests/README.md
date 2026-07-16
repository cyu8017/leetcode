# Test harness for 3368_first_letter_capitalization

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3368_first_letter_capitalization --language python
./scripts/test.sh --folder 3368_first_letter_capitalization --language javascript
./scripts/test.sh --folder 3368_first_letter_capitalization --language typescript
./scripts/test.sh --folder 3368_first_letter_capitalization --language java
./scripts/test.sh --folder 3368_first_letter_capitalization --language cpp
./scripts/test.sh --folder 3368_first_letter_capitalization --language c
./scripts/test.sh --folder 3368_first_letter_capitalization --language go
./scripts/test.sh --folder 3368_first_letter_capitalization --language rust
./scripts/test.sh --folder 3368_first_letter_capitalization --language kotlin
./scripts/test.sh --folder 3368_first_letter_capitalization --language swift
./scripts/test.sh --folder 3368_first_letter_capitalization --language ruby
./scripts/test.sh --folder 3368_first_letter_capitalization --language csharp
./scripts/test.sh --folder 3368_first_letter_capitalization --language scala
./scripts/test.sh --folder 3368_first_letter_capitalization --language php
./scripts/test.sh --folder 3368_first_letter_capitalization --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3368_first_letter_capitalization --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm java java 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm c c 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm go go 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm rust rust 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm swift swift 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm scala scala 3368_first_letter_capitalization
docker compose -f docker/docker-compose.yml run --rm php php 3368_first_letter_capitalization
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3368_first_letter_capitalization` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3368_first_letter_capitalization` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3368_first_letter_capitalization` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3368_first_letter_capitalization` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3368_first_letter_capitalization` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3368_first_letter_capitalization` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3368_first_letter_capitalization` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3368_first_letter_capitalization` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3368_first_letter_capitalization` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3368_first_letter_capitalization` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3368_first_letter_capitalization` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3368_first_letter_capitalization` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3368_first_letter_capitalization` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3368_first_letter_capitalization` |

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
.\scripts\test.ps1 -Folder 3368_first_letter_capitalization -AllLanguages
```

```bash
./scripts/test.sh --folder 3368_first_letter_capitalization --all-languages
```

```zsh
./scripts/test.sh --folder 3368_first_letter_capitalization --all-languages
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
