# Test harness for 2683_neighboring_bitwise_xor

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language python
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language javascript
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language typescript
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language java
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language cpp
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language c
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language go
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language rust
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language kotlin
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language swift
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language ruby
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language csharp
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language scala
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language php
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2683_neighboring_bitwise_xor --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm java java 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm c c 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm go go 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm rust rust 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm swift swift 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm scala scala 2683_neighboring_bitwise_xor
docker compose -f docker/docker-compose.yml run --rm php php 2683_neighboring_bitwise_xor
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2683_neighboring_bitwise_xor` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2683_neighboring_bitwise_xor` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2683_neighboring_bitwise_xor` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2683_neighboring_bitwise_xor` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2683_neighboring_bitwise_xor` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2683_neighboring_bitwise_xor` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2683_neighboring_bitwise_xor` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2683_neighboring_bitwise_xor` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2683_neighboring_bitwise_xor` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2683_neighboring_bitwise_xor` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2683_neighboring_bitwise_xor` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2683_neighboring_bitwise_xor` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2683_neighboring_bitwise_xor` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2683_neighboring_bitwise_xor` |

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
.\scripts\test.ps1 -Folder 2683_neighboring_bitwise_xor -AllLanguages
```

```bash
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --all-languages
```

```zsh
./scripts/test.sh --folder 2683_neighboring_bitwise_xor --all-languages
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
