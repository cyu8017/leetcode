# Test harness for 0722_remove_comments

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0722_remove_comments -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0722_remove_comments --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0722_remove_comments --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0722_remove_comments --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0722_remove_comments --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0722_remove_comments --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0722_remove_comments --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0722_remove_comments --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0722_remove_comments --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0722_remove_comments --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0722_remove_comments --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0722_remove_comments --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0722_remove_comments --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0722_remove_comments --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0722_remove_comments --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0722_remove_comments --language python
./scripts/test.sh --folder 0722_remove_comments --language javascript
./scripts/test.sh --folder 0722_remove_comments --language typescript
./scripts/test.sh --folder 0722_remove_comments --language java
./scripts/test.sh --folder 0722_remove_comments --language cpp
./scripts/test.sh --folder 0722_remove_comments --language c
./scripts/test.sh --folder 0722_remove_comments --language go
./scripts/test.sh --folder 0722_remove_comments --language rust
./scripts/test.sh --folder 0722_remove_comments --language kotlin
./scripts/test.sh --folder 0722_remove_comments --language swift
./scripts/test.sh --folder 0722_remove_comments --language ruby
./scripts/test.sh --folder 0722_remove_comments --language csharp
./scripts/test.sh --folder 0722_remove_comments --language scala
./scripts/test.sh --folder 0722_remove_comments --language php
./scripts/test.sh --folder 0722_remove_comments --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0722_remove_comments --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0722_remove_comments --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0722_remove_comments --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0722_remove_comments --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0722_remove_comments --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0722_remove_comments --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0722_remove_comments --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0722_remove_comments --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0722_remove_comments --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0722_remove_comments --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0722_remove_comments --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0722_remove_comments --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0722_remove_comments --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0722_remove_comments --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm java java 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm c c 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm go go 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm rust rust 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm swift swift 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm scala scala 0722_remove_comments
docker compose -f docker/docker-compose.yml run --rm php php 0722_remove_comments
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0722_remove_comments` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0722_remove_comments` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0722_remove_comments` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0722_remove_comments` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0722_remove_comments` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0722_remove_comments` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0722_remove_comments` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0722_remove_comments` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0722_remove_comments` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0722_remove_comments` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0722_remove_comments` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0722_remove_comments` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0722_remove_comments` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0722_remove_comments` |

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
.\scripts\test.ps1 -Folder 0722_remove_comments -AllLanguages
```

```bash
./scripts/test.sh --folder 0722_remove_comments --all-languages
```

```zsh
./scripts/test.sh --folder 0722_remove_comments --all-languages
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
