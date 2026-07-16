# Test harness for 1377_frog_position_after_t_seconds

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language python
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language javascript
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language typescript
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language java
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language cpp
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language c
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language go
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language rust
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language kotlin
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language swift
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language ruby
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language csharp
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language scala
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language php
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1377_frog_position_after_t_seconds --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm java java 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm c c 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm go go 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm rust rust 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm swift swift 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm scala scala 1377_frog_position_after_t_seconds
docker compose -f docker/docker-compose.yml run --rm php php 1377_frog_position_after_t_seconds
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1377_frog_position_after_t_seconds` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1377_frog_position_after_t_seconds` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1377_frog_position_after_t_seconds` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1377_frog_position_after_t_seconds` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1377_frog_position_after_t_seconds` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1377_frog_position_after_t_seconds` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1377_frog_position_after_t_seconds` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1377_frog_position_after_t_seconds` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1377_frog_position_after_t_seconds` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1377_frog_position_after_t_seconds` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1377_frog_position_after_t_seconds` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1377_frog_position_after_t_seconds` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1377_frog_position_after_t_seconds` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1377_frog_position_after_t_seconds` |

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
.\scripts\test.ps1 -Folder 1377_frog_position_after_t_seconds -AllLanguages
```

```bash
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --all-languages
```

```zsh
./scripts/test.sh --folder 1377_frog_position_after_t_seconds --all-languages
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
