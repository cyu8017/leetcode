# Test harness for 2967_minimum_cost_to_make_array_equalindromic

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language python
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language javascript
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language typescript
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language java
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language cpp
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language c
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language go
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language rust
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language kotlin
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language swift
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language ruby
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language csharp
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language scala
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language php
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm java java 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm c c 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm go go 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm rust rust 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm swift swift 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm scala scala 2967_minimum_cost_to_make_array_equalindromic
docker compose -f docker/docker-compose.yml run --rm php php 2967_minimum_cost_to_make_array_equalindromic
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2967_minimum_cost_to_make_array_equalindromic` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2967_minimum_cost_to_make_array_equalindromic` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2967_minimum_cost_to_make_array_equalindromic` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2967_minimum_cost_to_make_array_equalindromic` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2967_minimum_cost_to_make_array_equalindromic` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2967_minimum_cost_to_make_array_equalindromic` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2967_minimum_cost_to_make_array_equalindromic` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2967_minimum_cost_to_make_array_equalindromic` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2967_minimum_cost_to_make_array_equalindromic` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2967_minimum_cost_to_make_array_equalindromic` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2967_minimum_cost_to_make_array_equalindromic` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2967_minimum_cost_to_make_array_equalindromic` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2967_minimum_cost_to_make_array_equalindromic` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2967_minimum_cost_to_make_array_equalindromic` |

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
.\scripts\test.ps1 -Folder 2967_minimum_cost_to_make_array_equalindromic -AllLanguages
```

```bash
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --all-languages
```

```zsh
./scripts/test.sh --folder 2967_minimum_cost_to_make_array_equalindromic --all-languages
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
