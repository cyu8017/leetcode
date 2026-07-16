# Test harness for 0986_interval_list_intersections

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0986_interval_list_intersections -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0986_interval_list_intersections --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0986_interval_list_intersections --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0986_interval_list_intersections --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0986_interval_list_intersections --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0986_interval_list_intersections --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0986_interval_list_intersections --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0986_interval_list_intersections --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0986_interval_list_intersections --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0986_interval_list_intersections --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0986_interval_list_intersections --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0986_interval_list_intersections --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0986_interval_list_intersections --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0986_interval_list_intersections --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0986_interval_list_intersections --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0986_interval_list_intersections --language python
./scripts/test.sh --folder 0986_interval_list_intersections --language javascript
./scripts/test.sh --folder 0986_interval_list_intersections --language typescript
./scripts/test.sh --folder 0986_interval_list_intersections --language java
./scripts/test.sh --folder 0986_interval_list_intersections --language cpp
./scripts/test.sh --folder 0986_interval_list_intersections --language c
./scripts/test.sh --folder 0986_interval_list_intersections --language go
./scripts/test.sh --folder 0986_interval_list_intersections --language rust
./scripts/test.sh --folder 0986_interval_list_intersections --language kotlin
./scripts/test.sh --folder 0986_interval_list_intersections --language swift
./scripts/test.sh --folder 0986_interval_list_intersections --language ruby
./scripts/test.sh --folder 0986_interval_list_intersections --language csharp
./scripts/test.sh --folder 0986_interval_list_intersections --language scala
./scripts/test.sh --folder 0986_interval_list_intersections --language php
./scripts/test.sh --folder 0986_interval_list_intersections --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0986_interval_list_intersections --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0986_interval_list_intersections --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0986_interval_list_intersections --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0986_interval_list_intersections --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0986_interval_list_intersections --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0986_interval_list_intersections --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0986_interval_list_intersections --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0986_interval_list_intersections --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0986_interval_list_intersections --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0986_interval_list_intersections --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0986_interval_list_intersections --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0986_interval_list_intersections --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0986_interval_list_intersections --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0986_interval_list_intersections --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm java java 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm c c 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm go go 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm rust rust 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm swift swift 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm scala scala 0986_interval_list_intersections
docker compose -f docker/docker-compose.yml run --rm php php 0986_interval_list_intersections
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0986_interval_list_intersections` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0986_interval_list_intersections` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0986_interval_list_intersections` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0986_interval_list_intersections` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0986_interval_list_intersections` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0986_interval_list_intersections` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0986_interval_list_intersections` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0986_interval_list_intersections` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0986_interval_list_intersections` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0986_interval_list_intersections` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0986_interval_list_intersections` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0986_interval_list_intersections` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0986_interval_list_intersections` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0986_interval_list_intersections` |

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
.\scripts\test.ps1 -Folder 0986_interval_list_intersections -AllLanguages
```

```bash
./scripts/test.sh --folder 0986_interval_list_intersections --all-languages
```

```zsh
./scripts/test.sh --folder 0986_interval_list_intersections --all-languages
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
