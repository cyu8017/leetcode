# Test harness for 3991_sort_array_using_prefix_reversals

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language python
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language javascript
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language typescript
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language java
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language cpp
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language c
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language go
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language rust
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language kotlin
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language swift
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language ruby
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language csharp
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language scala
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language php
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm java java 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm c c 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm go go 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm rust rust 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm swift swift 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm scala scala 3991_sort_array_using_prefix_reversals
docker compose -f docker/docker-compose.yml run --rm php php 3991_sort_array_using_prefix_reversals
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3991_sort_array_using_prefix_reversals` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3991_sort_array_using_prefix_reversals` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3991_sort_array_using_prefix_reversals` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3991_sort_array_using_prefix_reversals` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3991_sort_array_using_prefix_reversals` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3991_sort_array_using_prefix_reversals` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3991_sort_array_using_prefix_reversals` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3991_sort_array_using_prefix_reversals` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3991_sort_array_using_prefix_reversals` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3991_sort_array_using_prefix_reversals` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3991_sort_array_using_prefix_reversals` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3991_sort_array_using_prefix_reversals` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3991_sort_array_using_prefix_reversals` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3991_sort_array_using_prefix_reversals` |

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
.\scripts\test.ps1 -Folder 3991_sort_array_using_prefix_reversals -AllLanguages
```

```bash
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --all-languages
```

```zsh
./scripts/test.sh --folder 3991_sort_array_using_prefix_reversals --all-languages
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
