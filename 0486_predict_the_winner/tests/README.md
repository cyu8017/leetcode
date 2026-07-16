# Test harness for 0486_predict_the_winner

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0486_predict_the_winner -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0486_predict_the_winner --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0486_predict_the_winner --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0486_predict_the_winner --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0486_predict_the_winner --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0486_predict_the_winner --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0486_predict_the_winner --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0486_predict_the_winner --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0486_predict_the_winner --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0486_predict_the_winner --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0486_predict_the_winner --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0486_predict_the_winner --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0486_predict_the_winner --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0486_predict_the_winner --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0486_predict_the_winner --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0486_predict_the_winner --language python
./scripts/test.sh --folder 0486_predict_the_winner --language javascript
./scripts/test.sh --folder 0486_predict_the_winner --language typescript
./scripts/test.sh --folder 0486_predict_the_winner --language java
./scripts/test.sh --folder 0486_predict_the_winner --language cpp
./scripts/test.sh --folder 0486_predict_the_winner --language c
./scripts/test.sh --folder 0486_predict_the_winner --language go
./scripts/test.sh --folder 0486_predict_the_winner --language rust
./scripts/test.sh --folder 0486_predict_the_winner --language kotlin
./scripts/test.sh --folder 0486_predict_the_winner --language swift
./scripts/test.sh --folder 0486_predict_the_winner --language ruby
./scripts/test.sh --folder 0486_predict_the_winner --language csharp
./scripts/test.sh --folder 0486_predict_the_winner --language scala
./scripts/test.sh --folder 0486_predict_the_winner --language php
./scripts/test.sh --folder 0486_predict_the_winner --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0486_predict_the_winner --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0486_predict_the_winner --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0486_predict_the_winner --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0486_predict_the_winner --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0486_predict_the_winner --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0486_predict_the_winner --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0486_predict_the_winner --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0486_predict_the_winner --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0486_predict_the_winner --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0486_predict_the_winner --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0486_predict_the_winner --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0486_predict_the_winner --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0486_predict_the_winner --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0486_predict_the_winner --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm java java 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm c c 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm go go 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm rust rust 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm swift swift 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm scala scala 0486_predict_the_winner
docker compose -f docker/docker-compose.yml run --rm php php 0486_predict_the_winner
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0486_predict_the_winner` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0486_predict_the_winner` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0486_predict_the_winner` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0486_predict_the_winner` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0486_predict_the_winner` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0486_predict_the_winner` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0486_predict_the_winner` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0486_predict_the_winner` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0486_predict_the_winner` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0486_predict_the_winner` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0486_predict_the_winner` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0486_predict_the_winner` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0486_predict_the_winner` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0486_predict_the_winner` |

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
.\scripts\test.ps1 -Folder 0486_predict_the_winner -AllLanguages
```

```bash
./scripts/test.sh --folder 0486_predict_the_winner --all-languages
```

```zsh
./scripts/test.sh --folder 0486_predict_the_winner --all-languages
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
