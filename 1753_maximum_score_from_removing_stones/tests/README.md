# Test harness for 1753_maximum_score_from_removing_stones

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language python
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language javascript
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language typescript
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language java
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language cpp
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language c
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language go
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language rust
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language kotlin
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language swift
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language ruby
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language csharp
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language scala
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language php
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm java java 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm c c 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm go go 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm rust rust 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm swift swift 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm scala scala 1753_maximum_score_from_removing_stones
docker compose -f docker/docker-compose.yml run --rm php php 1753_maximum_score_from_removing_stones
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1753_maximum_score_from_removing_stones` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1753_maximum_score_from_removing_stones` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1753_maximum_score_from_removing_stones` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1753_maximum_score_from_removing_stones` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1753_maximum_score_from_removing_stones` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1753_maximum_score_from_removing_stones` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1753_maximum_score_from_removing_stones` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1753_maximum_score_from_removing_stones` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1753_maximum_score_from_removing_stones` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1753_maximum_score_from_removing_stones` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1753_maximum_score_from_removing_stones` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1753_maximum_score_from_removing_stones` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1753_maximum_score_from_removing_stones` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1753_maximum_score_from_removing_stones` |

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
.\scripts\test.ps1 -Folder 1753_maximum_score_from_removing_stones -AllLanguages
```

```bash
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --all-languages
```

```zsh
./scripts/test.sh --folder 1753_maximum_score_from_removing_stones --all-languages
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
