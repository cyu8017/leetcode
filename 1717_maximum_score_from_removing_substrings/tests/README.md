# Test harness for 1717_maximum_score_from_removing_substrings

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language python
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language javascript
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language typescript
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language java
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language cpp
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language c
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language go
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language rust
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language kotlin
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language swift
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language ruby
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language csharp
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language scala
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language php
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm java java 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm c c 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm go go 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm rust rust 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm swift swift 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm scala scala 1717_maximum_score_from_removing_substrings
docker compose -f docker/docker-compose.yml run --rm php php 1717_maximum_score_from_removing_substrings
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1717_maximum_score_from_removing_substrings` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1717_maximum_score_from_removing_substrings` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1717_maximum_score_from_removing_substrings` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1717_maximum_score_from_removing_substrings` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1717_maximum_score_from_removing_substrings` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1717_maximum_score_from_removing_substrings` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1717_maximum_score_from_removing_substrings` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1717_maximum_score_from_removing_substrings` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1717_maximum_score_from_removing_substrings` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1717_maximum_score_from_removing_substrings` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1717_maximum_score_from_removing_substrings` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1717_maximum_score_from_removing_substrings` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1717_maximum_score_from_removing_substrings` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1717_maximum_score_from_removing_substrings` |

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
.\scripts\test.ps1 -Folder 1717_maximum_score_from_removing_substrings -AllLanguages
```

```bash
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --all-languages
```

```zsh
./scripts/test.sh --folder 1717_maximum_score_from_removing_substrings --all-languages
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
