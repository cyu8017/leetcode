# Test harness for 0860_lemonade_change

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0860_lemonade_change -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0860_lemonade_change --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0860_lemonade_change --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0860_lemonade_change --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0860_lemonade_change --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0860_lemonade_change --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0860_lemonade_change --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0860_lemonade_change --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0860_lemonade_change --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0860_lemonade_change --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0860_lemonade_change --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0860_lemonade_change --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0860_lemonade_change --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0860_lemonade_change --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0860_lemonade_change --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0860_lemonade_change --language python
./scripts/test.sh --folder 0860_lemonade_change --language javascript
./scripts/test.sh --folder 0860_lemonade_change --language typescript
./scripts/test.sh --folder 0860_lemonade_change --language java
./scripts/test.sh --folder 0860_lemonade_change --language cpp
./scripts/test.sh --folder 0860_lemonade_change --language c
./scripts/test.sh --folder 0860_lemonade_change --language go
./scripts/test.sh --folder 0860_lemonade_change --language rust
./scripts/test.sh --folder 0860_lemonade_change --language kotlin
./scripts/test.sh --folder 0860_lemonade_change --language swift
./scripts/test.sh --folder 0860_lemonade_change --language ruby
./scripts/test.sh --folder 0860_lemonade_change --language csharp
./scripts/test.sh --folder 0860_lemonade_change --language scala
./scripts/test.sh --folder 0860_lemonade_change --language php
./scripts/test.sh --folder 0860_lemonade_change --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0860_lemonade_change --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0860_lemonade_change --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0860_lemonade_change --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0860_lemonade_change --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0860_lemonade_change --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0860_lemonade_change --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0860_lemonade_change --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0860_lemonade_change --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0860_lemonade_change --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0860_lemonade_change --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0860_lemonade_change --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0860_lemonade_change --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0860_lemonade_change --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0860_lemonade_change --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm java java 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm c c 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm go go 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm rust rust 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm swift swift 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm scala scala 0860_lemonade_change
docker compose -f docker/docker-compose.yml run --rm php php 0860_lemonade_change
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0860_lemonade_change` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0860_lemonade_change` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0860_lemonade_change` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0860_lemonade_change` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0860_lemonade_change` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0860_lemonade_change` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0860_lemonade_change` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0860_lemonade_change` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0860_lemonade_change` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0860_lemonade_change` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0860_lemonade_change` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0860_lemonade_change` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0860_lemonade_change` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0860_lemonade_change` |

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
.\scripts\test.ps1 -Folder 0860_lemonade_change -AllLanguages
```

```bash
./scripts/test.sh --folder 0860_lemonade_change --all-languages
```

```zsh
./scripts/test.sh --folder 0860_lemonade_change --all-languages
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
