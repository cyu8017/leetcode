# Test harness for 3555_smallest_subarray_to_sort_in_every_sliding_window

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language python
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language javascript
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language typescript
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language java
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language cpp
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language c
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language go
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language rust
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language kotlin
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language swift
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language ruby
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language csharp
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language scala
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language php
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm java java 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm c c 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm go go 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm rust rust 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm swift swift 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm scala scala 3555_smallest_subarray_to_sort_in_every_sliding_window
docker compose -f docker/docker-compose.yml run --rm php php 3555_smallest_subarray_to_sort_in_every_sliding_window
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3555_smallest_subarray_to_sort_in_every_sliding_window` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3555_smallest_subarray_to_sort_in_every_sliding_window` |

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
.\scripts\test.ps1 -Folder 3555_smallest_subarray_to_sort_in_every_sliding_window -AllLanguages
```

```bash
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --all-languages
```

```zsh
./scripts/test.sh --folder 3555_smallest_subarray_to_sort_in_every_sliding_window --all-languages
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
