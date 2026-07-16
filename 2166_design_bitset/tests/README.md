# Test harness for 2166_design_bitset

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2166_design_bitset -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2166_design_bitset --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2166_design_bitset --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2166_design_bitset --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2166_design_bitset --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2166_design_bitset --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2166_design_bitset --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2166_design_bitset --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2166_design_bitset --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2166_design_bitset --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2166_design_bitset --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2166_design_bitset --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2166_design_bitset --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2166_design_bitset --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2166_design_bitset --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2166_design_bitset --language python
./scripts/test.sh --folder 2166_design_bitset --language javascript
./scripts/test.sh --folder 2166_design_bitset --language typescript
./scripts/test.sh --folder 2166_design_bitset --language java
./scripts/test.sh --folder 2166_design_bitset --language cpp
./scripts/test.sh --folder 2166_design_bitset --language c
./scripts/test.sh --folder 2166_design_bitset --language go
./scripts/test.sh --folder 2166_design_bitset --language rust
./scripts/test.sh --folder 2166_design_bitset --language kotlin
./scripts/test.sh --folder 2166_design_bitset --language swift
./scripts/test.sh --folder 2166_design_bitset --language ruby
./scripts/test.sh --folder 2166_design_bitset --language csharp
./scripts/test.sh --folder 2166_design_bitset --language scala
./scripts/test.sh --folder 2166_design_bitset --language php
./scripts/test.sh --folder 2166_design_bitset --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2166_design_bitset --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2166_design_bitset --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2166_design_bitset --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2166_design_bitset --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2166_design_bitset --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2166_design_bitset --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2166_design_bitset --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2166_design_bitset --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2166_design_bitset --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2166_design_bitset --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2166_design_bitset --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2166_design_bitset --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2166_design_bitset --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2166_design_bitset --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm java java 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm c c 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm go go 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm rust rust 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm swift swift 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm scala scala 2166_design_bitset
docker compose -f docker/docker-compose.yml run --rm php php 2166_design_bitset
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2166_design_bitset` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2166_design_bitset` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2166_design_bitset` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2166_design_bitset` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2166_design_bitset` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2166_design_bitset` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2166_design_bitset` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2166_design_bitset` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2166_design_bitset` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2166_design_bitset` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2166_design_bitset` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2166_design_bitset` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2166_design_bitset` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2166_design_bitset` |

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
.\scripts\test.ps1 -Folder 2166_design_bitset -AllLanguages
```

```bash
./scripts/test.sh --folder 2166_design_bitset --all-languages
```

```zsh
./scripts/test.sh --folder 2166_design_bitset --all-languages
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
