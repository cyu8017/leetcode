# Test harness for 3401_find_circular_gift_exchange_chains

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language python
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language javascript
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language typescript
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language java
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language cpp
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language c
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language go
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language rust
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language kotlin
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language swift
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language ruby
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language csharp
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language scala
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language php
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm java java 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm c c 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm go go 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm rust rust 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm swift swift 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm scala scala 3401_find_circular_gift_exchange_chains
docker compose -f docker/docker-compose.yml run --rm php php 3401_find_circular_gift_exchange_chains
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3401_find_circular_gift_exchange_chains` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3401_find_circular_gift_exchange_chains` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3401_find_circular_gift_exchange_chains` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3401_find_circular_gift_exchange_chains` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3401_find_circular_gift_exchange_chains` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3401_find_circular_gift_exchange_chains` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3401_find_circular_gift_exchange_chains` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3401_find_circular_gift_exchange_chains` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3401_find_circular_gift_exchange_chains` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3401_find_circular_gift_exchange_chains` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3401_find_circular_gift_exchange_chains` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3401_find_circular_gift_exchange_chains` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3401_find_circular_gift_exchange_chains` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3401_find_circular_gift_exchange_chains` |

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
.\scripts\test.ps1 -Folder 3401_find_circular_gift_exchange_chains -AllLanguages
```

```bash
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --all-languages
```

```zsh
./scripts/test.sh --folder 3401_find_circular_gift_exchange_chains --all-languages
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
