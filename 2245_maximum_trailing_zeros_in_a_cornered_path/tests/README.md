# Test harness for 2245_maximum_trailing_zeros_in_a_cornered_path

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language python
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language javascript
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language typescript
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language java
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language cpp
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language c
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language go
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language rust
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language kotlin
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language swift
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language ruby
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language csharp
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language scala
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language php
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm java java 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm c c 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm go go 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm rust rust 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm swift swift 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm scala scala 2245_maximum_trailing_zeros_in_a_cornered_path
docker compose -f docker/docker-compose.yml run --rm php php 2245_maximum_trailing_zeros_in_a_cornered_path
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2245_maximum_trailing_zeros_in_a_cornered_path` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2245_maximum_trailing_zeros_in_a_cornered_path` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2245_maximum_trailing_zeros_in_a_cornered_path` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2245_maximum_trailing_zeros_in_a_cornered_path` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2245_maximum_trailing_zeros_in_a_cornered_path` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2245_maximum_trailing_zeros_in_a_cornered_path` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2245_maximum_trailing_zeros_in_a_cornered_path` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2245_maximum_trailing_zeros_in_a_cornered_path` |

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
.\scripts\test.ps1 -Folder 2245_maximum_trailing_zeros_in_a_cornered_path -AllLanguages
```

```bash
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --all-languages
```

```zsh
./scripts/test.sh --folder 2245_maximum_trailing_zeros_in_a_cornered_path --all-languages
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
