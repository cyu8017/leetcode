# Test harness for 1144_decrease_elements_to_make_array_zigzag

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language python
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language javascript
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language typescript
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language java
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language cpp
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language c
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language go
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language rust
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language kotlin
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language swift
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language ruby
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language csharp
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language scala
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language php
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm java java 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm c c 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm go go 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm rust rust 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm swift swift 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm scala scala 1144_decrease_elements_to_make_array_zigzag
docker compose -f docker/docker-compose.yml run --rm php php 1144_decrease_elements_to_make_array_zigzag
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1144_decrease_elements_to_make_array_zigzag` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1144_decrease_elements_to_make_array_zigzag` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1144_decrease_elements_to_make_array_zigzag` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1144_decrease_elements_to_make_array_zigzag` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1144_decrease_elements_to_make_array_zigzag` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1144_decrease_elements_to_make_array_zigzag` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1144_decrease_elements_to_make_array_zigzag` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1144_decrease_elements_to_make_array_zigzag` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1144_decrease_elements_to_make_array_zigzag` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1144_decrease_elements_to_make_array_zigzag` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1144_decrease_elements_to_make_array_zigzag` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1144_decrease_elements_to_make_array_zigzag` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1144_decrease_elements_to_make_array_zigzag` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1144_decrease_elements_to_make_array_zigzag` |

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
.\scripts\test.ps1 -Folder 1144_decrease_elements_to_make_array_zigzag -AllLanguages
```

```bash
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --all-languages
```

```zsh
./scripts/test.sh --folder 1144_decrease_elements_to_make_array_zigzag --all-languages
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
