# Test harness for 1574_shortest_subarray_to_be_removed_to_make_array_sorted

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language python
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language javascript
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language typescript
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language java
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language cpp
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language c
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language go
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language rust
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language kotlin
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language swift
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language ruby
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language csharp
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language scala
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language php
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm java java 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm c c 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm go go 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm rust rust 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm swift swift 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm scala scala 1574_shortest_subarray_to_be_removed_to_make_array_sorted
docker compose -f docker/docker-compose.yml run --rm php php 1574_shortest_subarray_to_be_removed_to_make_array_sorted
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1574_shortest_subarray_to_be_removed_to_make_array_sorted` |

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
.\scripts\test.ps1 -Folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted -AllLanguages
```

```bash
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --all-languages
```

```zsh
./scripts/test.sh --folder 1574_shortest_subarray_to_be_removed_to_make_array_sorted --all-languages
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
