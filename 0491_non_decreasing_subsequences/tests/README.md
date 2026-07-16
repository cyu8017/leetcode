# Test harness for 0491_non_decreasing_subsequences

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language python
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language javascript
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language typescript
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language java
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language cpp
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language c
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language go
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language rust
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language kotlin
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language swift
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language ruby
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language csharp
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language scala
./scripts/test.sh --folder 0491_non_decreasing_subsequences --language php
./scripts/test.sh --folder 0491_non_decreasing_subsequences --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0491_non_decreasing_subsequences --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm java java 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm c c 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm go go 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm rust rust 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm swift swift 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm scala scala 0491_non_decreasing_subsequences
docker compose -f docker/docker-compose.yml run --rm php php 0491_non_decreasing_subsequences
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0491_non_decreasing_subsequences` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0491_non_decreasing_subsequences` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0491_non_decreasing_subsequences` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0491_non_decreasing_subsequences` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0491_non_decreasing_subsequences` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0491_non_decreasing_subsequences` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0491_non_decreasing_subsequences` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0491_non_decreasing_subsequences` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0491_non_decreasing_subsequences` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0491_non_decreasing_subsequences` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0491_non_decreasing_subsequences` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0491_non_decreasing_subsequences` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0491_non_decreasing_subsequences` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0491_non_decreasing_subsequences` |

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
.\scripts\test.ps1 -Folder 0491_non_decreasing_subsequences -AllLanguages
```

```bash
./scripts/test.sh --folder 0491_non_decreasing_subsequences --all-languages
```

```zsh
./scripts/test.sh --folder 0491_non_decreasing_subsequences --all-languages
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
