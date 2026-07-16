# Test harness for 2826_sorting_three_groups

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2826_sorting_three_groups -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2826_sorting_three_groups --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2826_sorting_three_groups --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2826_sorting_three_groups --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2826_sorting_three_groups --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2826_sorting_three_groups --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2826_sorting_three_groups --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2826_sorting_three_groups --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2826_sorting_three_groups --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2826_sorting_three_groups --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2826_sorting_three_groups --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2826_sorting_three_groups --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2826_sorting_three_groups --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2826_sorting_three_groups --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2826_sorting_three_groups --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2826_sorting_three_groups --language python
./scripts/test.sh --folder 2826_sorting_three_groups --language javascript
./scripts/test.sh --folder 2826_sorting_three_groups --language typescript
./scripts/test.sh --folder 2826_sorting_three_groups --language java
./scripts/test.sh --folder 2826_sorting_three_groups --language cpp
./scripts/test.sh --folder 2826_sorting_three_groups --language c
./scripts/test.sh --folder 2826_sorting_three_groups --language go
./scripts/test.sh --folder 2826_sorting_three_groups --language rust
./scripts/test.sh --folder 2826_sorting_three_groups --language kotlin
./scripts/test.sh --folder 2826_sorting_three_groups --language swift
./scripts/test.sh --folder 2826_sorting_three_groups --language ruby
./scripts/test.sh --folder 2826_sorting_three_groups --language csharp
./scripts/test.sh --folder 2826_sorting_three_groups --language scala
./scripts/test.sh --folder 2826_sorting_three_groups --language php
./scripts/test.sh --folder 2826_sorting_three_groups --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2826_sorting_three_groups --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2826_sorting_three_groups --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2826_sorting_three_groups --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2826_sorting_three_groups --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2826_sorting_three_groups --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2826_sorting_three_groups --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2826_sorting_three_groups --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2826_sorting_three_groups --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2826_sorting_three_groups --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2826_sorting_three_groups --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2826_sorting_three_groups --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2826_sorting_three_groups --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2826_sorting_three_groups --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2826_sorting_three_groups --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm java java 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm c c 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm go go 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm rust rust 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm swift swift 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm scala scala 2826_sorting_three_groups
docker compose -f docker/docker-compose.yml run --rm php php 2826_sorting_three_groups
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2826_sorting_three_groups` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2826_sorting_three_groups` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2826_sorting_three_groups` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2826_sorting_three_groups` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2826_sorting_three_groups` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2826_sorting_three_groups` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2826_sorting_three_groups` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2826_sorting_three_groups` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2826_sorting_three_groups` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2826_sorting_three_groups` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2826_sorting_three_groups` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2826_sorting_three_groups` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2826_sorting_three_groups` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2826_sorting_three_groups` |

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
.\scripts\test.ps1 -Folder 2826_sorting_three_groups -AllLanguages
```

```bash
./scripts/test.sh --folder 2826_sorting_three_groups --all-languages
```

```zsh
./scripts/test.sh --folder 2826_sorting_three_groups --all-languages
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
