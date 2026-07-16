# Test harness for 1046_last_stone_weight

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1046_last_stone_weight -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1046_last_stone_weight --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1046_last_stone_weight --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1046_last_stone_weight --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1046_last_stone_weight --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1046_last_stone_weight --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1046_last_stone_weight --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1046_last_stone_weight --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1046_last_stone_weight --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1046_last_stone_weight --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1046_last_stone_weight --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1046_last_stone_weight --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1046_last_stone_weight --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1046_last_stone_weight --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1046_last_stone_weight --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1046_last_stone_weight --language python
./scripts/test.sh --folder 1046_last_stone_weight --language javascript
./scripts/test.sh --folder 1046_last_stone_weight --language typescript
./scripts/test.sh --folder 1046_last_stone_weight --language java
./scripts/test.sh --folder 1046_last_stone_weight --language cpp
./scripts/test.sh --folder 1046_last_stone_weight --language c
./scripts/test.sh --folder 1046_last_stone_weight --language go
./scripts/test.sh --folder 1046_last_stone_weight --language rust
./scripts/test.sh --folder 1046_last_stone_weight --language kotlin
./scripts/test.sh --folder 1046_last_stone_weight --language swift
./scripts/test.sh --folder 1046_last_stone_weight --language ruby
./scripts/test.sh --folder 1046_last_stone_weight --language csharp
./scripts/test.sh --folder 1046_last_stone_weight --language scala
./scripts/test.sh --folder 1046_last_stone_weight --language php
./scripts/test.sh --folder 1046_last_stone_weight --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1046_last_stone_weight --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1046_last_stone_weight --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1046_last_stone_weight --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1046_last_stone_weight --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1046_last_stone_weight --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1046_last_stone_weight --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1046_last_stone_weight --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1046_last_stone_weight --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1046_last_stone_weight --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1046_last_stone_weight --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1046_last_stone_weight --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1046_last_stone_weight --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1046_last_stone_weight --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1046_last_stone_weight --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm java java 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm c c 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm go go 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm rust rust 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm swift swift 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm scala scala 1046_last_stone_weight
docker compose -f docker/docker-compose.yml run --rm php php 1046_last_stone_weight
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1046_last_stone_weight` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1046_last_stone_weight` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1046_last_stone_weight` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1046_last_stone_weight` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1046_last_stone_weight` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1046_last_stone_weight` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1046_last_stone_weight` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1046_last_stone_weight` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1046_last_stone_weight` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1046_last_stone_weight` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1046_last_stone_weight` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1046_last_stone_weight` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1046_last_stone_weight` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1046_last_stone_weight` |

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
.\scripts\test.ps1 -Folder 1046_last_stone_weight -AllLanguages
```

```bash
./scripts/test.sh --folder 1046_last_stone_weight --all-languages
```

```zsh
./scripts/test.sh --folder 1046_last_stone_weight --all-languages
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
