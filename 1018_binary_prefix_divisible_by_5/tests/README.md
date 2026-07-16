# Test harness for 1018_binary_prefix_divisible_by_5

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language python
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language javascript
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language typescript
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language java
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language cpp
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language c
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language go
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language rust
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language kotlin
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language swift
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language ruby
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language csharp
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language scala
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language php
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm java java 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm c c 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm go go 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm rust rust 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm swift swift 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm scala scala 1018_binary_prefix_divisible_by_5
docker compose -f docker/docker-compose.yml run --rm php php 1018_binary_prefix_divisible_by_5
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1018_binary_prefix_divisible_by_5` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1018_binary_prefix_divisible_by_5` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1018_binary_prefix_divisible_by_5` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1018_binary_prefix_divisible_by_5` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1018_binary_prefix_divisible_by_5` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1018_binary_prefix_divisible_by_5` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1018_binary_prefix_divisible_by_5` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1018_binary_prefix_divisible_by_5` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1018_binary_prefix_divisible_by_5` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1018_binary_prefix_divisible_by_5` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1018_binary_prefix_divisible_by_5` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1018_binary_prefix_divisible_by_5` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1018_binary_prefix_divisible_by_5` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1018_binary_prefix_divisible_by_5` |

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
.\scripts\test.ps1 -Folder 1018_binary_prefix_divisible_by_5 -AllLanguages
```

```bash
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --all-languages
```

```zsh
./scripts/test.sh --folder 1018_binary_prefix_divisible_by_5 --all-languages
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
