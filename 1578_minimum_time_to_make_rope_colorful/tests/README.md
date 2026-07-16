# Test harness for 1578_minimum_time_to_make_rope_colorful

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language python
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language javascript
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language typescript
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language java
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language cpp
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language c
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language go
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language rust
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language kotlin
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language swift
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language ruby
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language csharp
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language scala
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language php
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm java java 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm c c 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm go go 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm rust rust 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm swift swift 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm scala scala 1578_minimum_time_to_make_rope_colorful
docker compose -f docker/docker-compose.yml run --rm php php 1578_minimum_time_to_make_rope_colorful
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1578_minimum_time_to_make_rope_colorful` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1578_minimum_time_to_make_rope_colorful` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1578_minimum_time_to_make_rope_colorful` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1578_minimum_time_to_make_rope_colorful` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1578_minimum_time_to_make_rope_colorful` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1578_minimum_time_to_make_rope_colorful` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1578_minimum_time_to_make_rope_colorful` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1578_minimum_time_to_make_rope_colorful` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1578_minimum_time_to_make_rope_colorful` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1578_minimum_time_to_make_rope_colorful` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1578_minimum_time_to_make_rope_colorful` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1578_minimum_time_to_make_rope_colorful` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1578_minimum_time_to_make_rope_colorful` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1578_minimum_time_to_make_rope_colorful` |

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
.\scripts\test.ps1 -Folder 1578_minimum_time_to_make_rope_colorful -AllLanguages
```

```bash
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --all-languages
```

```zsh
./scripts/test.sh --folder 1578_minimum_time_to_make_rope_colorful --all-languages
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
