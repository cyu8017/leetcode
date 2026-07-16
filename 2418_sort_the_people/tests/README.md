# Test harness for 2418_sort_the_people

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2418_sort_the_people -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2418_sort_the_people --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2418_sort_the_people --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2418_sort_the_people --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2418_sort_the_people --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2418_sort_the_people --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2418_sort_the_people --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2418_sort_the_people --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2418_sort_the_people --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2418_sort_the_people --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2418_sort_the_people --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2418_sort_the_people --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2418_sort_the_people --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2418_sort_the_people --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2418_sort_the_people --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2418_sort_the_people --language python
./scripts/test.sh --folder 2418_sort_the_people --language javascript
./scripts/test.sh --folder 2418_sort_the_people --language typescript
./scripts/test.sh --folder 2418_sort_the_people --language java
./scripts/test.sh --folder 2418_sort_the_people --language cpp
./scripts/test.sh --folder 2418_sort_the_people --language c
./scripts/test.sh --folder 2418_sort_the_people --language go
./scripts/test.sh --folder 2418_sort_the_people --language rust
./scripts/test.sh --folder 2418_sort_the_people --language kotlin
./scripts/test.sh --folder 2418_sort_the_people --language swift
./scripts/test.sh --folder 2418_sort_the_people --language ruby
./scripts/test.sh --folder 2418_sort_the_people --language csharp
./scripts/test.sh --folder 2418_sort_the_people --language scala
./scripts/test.sh --folder 2418_sort_the_people --language php
./scripts/test.sh --folder 2418_sort_the_people --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2418_sort_the_people --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2418_sort_the_people --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2418_sort_the_people --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2418_sort_the_people --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2418_sort_the_people --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2418_sort_the_people --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2418_sort_the_people --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2418_sort_the_people --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2418_sort_the_people --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2418_sort_the_people --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2418_sort_the_people --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2418_sort_the_people --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2418_sort_the_people --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2418_sort_the_people --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm java java 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm c c 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm go go 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm rust rust 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm swift swift 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm scala scala 2418_sort_the_people
docker compose -f docker/docker-compose.yml run --rm php php 2418_sort_the_people
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2418_sort_the_people` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2418_sort_the_people` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2418_sort_the_people` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2418_sort_the_people` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2418_sort_the_people` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2418_sort_the_people` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2418_sort_the_people` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2418_sort_the_people` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2418_sort_the_people` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2418_sort_the_people` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2418_sort_the_people` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2418_sort_the_people` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2418_sort_the_people` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2418_sort_the_people` |

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
.\scripts\test.ps1 -Folder 2418_sort_the_people -AllLanguages
```

```bash
./scripts/test.sh --folder 2418_sort_the_people --all-languages
```

```zsh
./scripts/test.sh --folder 2418_sort_the_people --all-languages
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
