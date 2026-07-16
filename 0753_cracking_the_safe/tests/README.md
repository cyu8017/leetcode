# Test harness for 0753_cracking_the_safe

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0753_cracking_the_safe -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0753_cracking_the_safe --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0753_cracking_the_safe --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0753_cracking_the_safe --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0753_cracking_the_safe --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0753_cracking_the_safe --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0753_cracking_the_safe --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0753_cracking_the_safe --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0753_cracking_the_safe --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0753_cracking_the_safe --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0753_cracking_the_safe --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0753_cracking_the_safe --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0753_cracking_the_safe --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0753_cracking_the_safe --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0753_cracking_the_safe --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0753_cracking_the_safe --language python
./scripts/test.sh --folder 0753_cracking_the_safe --language javascript
./scripts/test.sh --folder 0753_cracking_the_safe --language typescript
./scripts/test.sh --folder 0753_cracking_the_safe --language java
./scripts/test.sh --folder 0753_cracking_the_safe --language cpp
./scripts/test.sh --folder 0753_cracking_the_safe --language c
./scripts/test.sh --folder 0753_cracking_the_safe --language go
./scripts/test.sh --folder 0753_cracking_the_safe --language rust
./scripts/test.sh --folder 0753_cracking_the_safe --language kotlin
./scripts/test.sh --folder 0753_cracking_the_safe --language swift
./scripts/test.sh --folder 0753_cracking_the_safe --language ruby
./scripts/test.sh --folder 0753_cracking_the_safe --language csharp
./scripts/test.sh --folder 0753_cracking_the_safe --language scala
./scripts/test.sh --folder 0753_cracking_the_safe --language php
./scripts/test.sh --folder 0753_cracking_the_safe --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0753_cracking_the_safe --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0753_cracking_the_safe --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0753_cracking_the_safe --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0753_cracking_the_safe --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0753_cracking_the_safe --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0753_cracking_the_safe --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0753_cracking_the_safe --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0753_cracking_the_safe --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0753_cracking_the_safe --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0753_cracking_the_safe --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0753_cracking_the_safe --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0753_cracking_the_safe --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0753_cracking_the_safe --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0753_cracking_the_safe --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm java java 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm c c 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm go go 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm rust rust 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm swift swift 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm scala scala 0753_cracking_the_safe
docker compose -f docker/docker-compose.yml run --rm php php 0753_cracking_the_safe
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0753_cracking_the_safe` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0753_cracking_the_safe` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0753_cracking_the_safe` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0753_cracking_the_safe` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0753_cracking_the_safe` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0753_cracking_the_safe` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0753_cracking_the_safe` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0753_cracking_the_safe` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0753_cracking_the_safe` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0753_cracking_the_safe` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0753_cracking_the_safe` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0753_cracking_the_safe` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0753_cracking_the_safe` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0753_cracking_the_safe` |

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
.\scripts\test.ps1 -Folder 0753_cracking_the_safe -AllLanguages
```

```bash
./scripts/test.sh --folder 0753_cracking_the_safe --all-languages
```

```zsh
./scripts/test.sh --folder 0753_cracking_the_safe --all-languages
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
