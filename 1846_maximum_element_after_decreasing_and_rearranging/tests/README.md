# Test harness for 1846_maximum_element_after_decreasing_and_rearranging

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language python
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language javascript
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language typescript
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language java
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language cpp
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language c
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language go
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language rust
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language kotlin
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language swift
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language ruby
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language csharp
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language scala
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language php
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm java java 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm c c 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm go go 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm rust rust 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm swift swift 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm scala scala 1846_maximum_element_after_decreasing_and_rearranging
docker compose -f docker/docker-compose.yml run --rm php php 1846_maximum_element_after_decreasing_and_rearranging
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1846_maximum_element_after_decreasing_and_rearranging` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1846_maximum_element_after_decreasing_and_rearranging` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1846_maximum_element_after_decreasing_and_rearranging` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1846_maximum_element_after_decreasing_and_rearranging` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1846_maximum_element_after_decreasing_and_rearranging` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1846_maximum_element_after_decreasing_and_rearranging` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1846_maximum_element_after_decreasing_and_rearranging` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1846_maximum_element_after_decreasing_and_rearranging` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1846_maximum_element_after_decreasing_and_rearranging` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1846_maximum_element_after_decreasing_and_rearranging` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1846_maximum_element_after_decreasing_and_rearranging` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1846_maximum_element_after_decreasing_and_rearranging` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1846_maximum_element_after_decreasing_and_rearranging` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1846_maximum_element_after_decreasing_and_rearranging` |

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
.\scripts\test.ps1 -Folder 1846_maximum_element_after_decreasing_and_rearranging -AllLanguages
```

```bash
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --all-languages
```

```zsh
./scripts/test.sh --folder 1846_maximum_element_after_decreasing_and_rearranging --all-languages
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
