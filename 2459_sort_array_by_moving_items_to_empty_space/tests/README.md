# Test harness for 2459_sort_array_by_moving_items_to_empty_space

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language python
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language javascript
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language typescript
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language java
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language cpp
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language c
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language go
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language rust
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language kotlin
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language swift
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language ruby
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language csharp
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language scala
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language php
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm java java 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm c c 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm go go 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm rust rust 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm swift swift 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm scala scala 2459_sort_array_by_moving_items_to_empty_space
docker compose -f docker/docker-compose.yml run --rm php php 2459_sort_array_by_moving_items_to_empty_space
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2459_sort_array_by_moving_items_to_empty_space` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2459_sort_array_by_moving_items_to_empty_space` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2459_sort_array_by_moving_items_to_empty_space` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2459_sort_array_by_moving_items_to_empty_space` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2459_sort_array_by_moving_items_to_empty_space` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2459_sort_array_by_moving_items_to_empty_space` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2459_sort_array_by_moving_items_to_empty_space` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2459_sort_array_by_moving_items_to_empty_space` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2459_sort_array_by_moving_items_to_empty_space` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2459_sort_array_by_moving_items_to_empty_space` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2459_sort_array_by_moving_items_to_empty_space` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2459_sort_array_by_moving_items_to_empty_space` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2459_sort_array_by_moving_items_to_empty_space` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2459_sort_array_by_moving_items_to_empty_space` |

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
.\scripts\test.ps1 -Folder 2459_sort_array_by_moving_items_to_empty_space -AllLanguages
```

```bash
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --all-languages
```

```zsh
./scripts/test.sh --folder 2459_sort_array_by_moving_items_to_empty_space --all-languages
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
