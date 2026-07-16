# Test harness for 2379_minimum_recolors_to_get_k_consecutive_black_blocks

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language python
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language javascript
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language typescript
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language java
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language cpp
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language c
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language go
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language rust
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language kotlin
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language swift
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language ruby
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language csharp
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language scala
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language php
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm java java 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm c c 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm go go 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm rust rust 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm swift swift 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm scala scala 2379_minimum_recolors_to_get_k_consecutive_black_blocks
docker compose -f docker/docker-compose.yml run --rm php php 2379_minimum_recolors_to_get_k_consecutive_black_blocks
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2379_minimum_recolors_to_get_k_consecutive_black_blocks` |

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
.\scripts\test.ps1 -Folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks -AllLanguages
```

```bash
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --all-languages
```

```zsh
./scripts/test.sh --folder 2379_minimum_recolors_to_get_k_consecutive_black_blocks --all-languages
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
