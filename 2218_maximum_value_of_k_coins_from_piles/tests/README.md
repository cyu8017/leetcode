# Test harness for 2218_maximum_value_of_k_coins_from_piles

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language python
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language javascript
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language typescript
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language java
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language cpp
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language c
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language go
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language rust
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language kotlin
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language swift
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language ruby
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language csharp
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language scala
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language php
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm java java 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm c c 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm go go 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm rust rust 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm swift swift 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm scala scala 2218_maximum_value_of_k_coins_from_piles
docker compose -f docker/docker-compose.yml run --rm php php 2218_maximum_value_of_k_coins_from_piles
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2218_maximum_value_of_k_coins_from_piles` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2218_maximum_value_of_k_coins_from_piles` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2218_maximum_value_of_k_coins_from_piles` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2218_maximum_value_of_k_coins_from_piles` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2218_maximum_value_of_k_coins_from_piles` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2218_maximum_value_of_k_coins_from_piles` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2218_maximum_value_of_k_coins_from_piles` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2218_maximum_value_of_k_coins_from_piles` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2218_maximum_value_of_k_coins_from_piles` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2218_maximum_value_of_k_coins_from_piles` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2218_maximum_value_of_k_coins_from_piles` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2218_maximum_value_of_k_coins_from_piles` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2218_maximum_value_of_k_coins_from_piles` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2218_maximum_value_of_k_coins_from_piles` |

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
.\scripts\test.ps1 -Folder 2218_maximum_value_of_k_coins_from_piles -AllLanguages
```

```bash
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --all-languages
```

```zsh
./scripts/test.sh --folder 2218_maximum_value_of_k_coins_from_piles --all-languages
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
