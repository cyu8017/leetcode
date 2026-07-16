# Test harness for 0277_find_the_celebrity

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0277_find_the_celebrity -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0277_find_the_celebrity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0277_find_the_celebrity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0277_find_the_celebrity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0277_find_the_celebrity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0277_find_the_celebrity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0277_find_the_celebrity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0277_find_the_celebrity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0277_find_the_celebrity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0277_find_the_celebrity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0277_find_the_celebrity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0277_find_the_celebrity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0277_find_the_celebrity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0277_find_the_celebrity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0277_find_the_celebrity --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0277_find_the_celebrity --language python
./scripts/test.sh --folder 0277_find_the_celebrity --language javascript
./scripts/test.sh --folder 0277_find_the_celebrity --language typescript
./scripts/test.sh --folder 0277_find_the_celebrity --language java
./scripts/test.sh --folder 0277_find_the_celebrity --language cpp
./scripts/test.sh --folder 0277_find_the_celebrity --language c
./scripts/test.sh --folder 0277_find_the_celebrity --language go
./scripts/test.sh --folder 0277_find_the_celebrity --language rust
./scripts/test.sh --folder 0277_find_the_celebrity --language kotlin
./scripts/test.sh --folder 0277_find_the_celebrity --language swift
./scripts/test.sh --folder 0277_find_the_celebrity --language ruby
./scripts/test.sh --folder 0277_find_the_celebrity --language csharp
./scripts/test.sh --folder 0277_find_the_celebrity --language scala
./scripts/test.sh --folder 0277_find_the_celebrity --language php
./scripts/test.sh --folder 0277_find_the_celebrity --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0277_find_the_celebrity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0277_find_the_celebrity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0277_find_the_celebrity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0277_find_the_celebrity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0277_find_the_celebrity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0277_find_the_celebrity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0277_find_the_celebrity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0277_find_the_celebrity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0277_find_the_celebrity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0277_find_the_celebrity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0277_find_the_celebrity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0277_find_the_celebrity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0277_find_the_celebrity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0277_find_the_celebrity --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm java java 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm c c 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm go go 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm rust rust 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm swift swift 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm scala scala 0277_find_the_celebrity
docker compose -f docker/docker-compose.yml run --rm php php 0277_find_the_celebrity
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0277_find_the_celebrity` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0277_find_the_celebrity` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0277_find_the_celebrity` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0277_find_the_celebrity` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0277_find_the_celebrity` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0277_find_the_celebrity` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0277_find_the_celebrity` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0277_find_the_celebrity` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0277_find_the_celebrity` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0277_find_the_celebrity` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0277_find_the_celebrity` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0277_find_the_celebrity` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0277_find_the_celebrity` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0277_find_the_celebrity` |

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
.\scripts\test.ps1 -Folder 0277_find_the_celebrity -AllLanguages
```

```bash
./scripts/test.sh --folder 0277_find_the_celebrity --all-languages
```

```zsh
./scripts/test.sh --folder 0277_find_the_celebrity --all-languages
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
