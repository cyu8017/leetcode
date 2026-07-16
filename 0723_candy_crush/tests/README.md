# Test harness for 0723_candy_crush

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0723_candy_crush -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0723_candy_crush --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0723_candy_crush --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0723_candy_crush --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0723_candy_crush --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0723_candy_crush --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0723_candy_crush --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0723_candy_crush --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0723_candy_crush --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0723_candy_crush --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0723_candy_crush --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0723_candy_crush --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0723_candy_crush --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0723_candy_crush --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0723_candy_crush --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0723_candy_crush --language python
./scripts/test.sh --folder 0723_candy_crush --language javascript
./scripts/test.sh --folder 0723_candy_crush --language typescript
./scripts/test.sh --folder 0723_candy_crush --language java
./scripts/test.sh --folder 0723_candy_crush --language cpp
./scripts/test.sh --folder 0723_candy_crush --language c
./scripts/test.sh --folder 0723_candy_crush --language go
./scripts/test.sh --folder 0723_candy_crush --language rust
./scripts/test.sh --folder 0723_candy_crush --language kotlin
./scripts/test.sh --folder 0723_candy_crush --language swift
./scripts/test.sh --folder 0723_candy_crush --language ruby
./scripts/test.sh --folder 0723_candy_crush --language csharp
./scripts/test.sh --folder 0723_candy_crush --language scala
./scripts/test.sh --folder 0723_candy_crush --language php
./scripts/test.sh --folder 0723_candy_crush --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0723_candy_crush --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0723_candy_crush --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0723_candy_crush --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0723_candy_crush --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0723_candy_crush --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0723_candy_crush --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0723_candy_crush --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0723_candy_crush --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0723_candy_crush --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0723_candy_crush --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0723_candy_crush --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0723_candy_crush --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0723_candy_crush --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0723_candy_crush --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm java java 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm c c 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm go go 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm rust rust 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm swift swift 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm scala scala 0723_candy_crush
docker compose -f docker/docker-compose.yml run --rm php php 0723_candy_crush
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0723_candy_crush` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0723_candy_crush` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0723_candy_crush` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0723_candy_crush` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0723_candy_crush` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0723_candy_crush` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0723_candy_crush` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0723_candy_crush` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0723_candy_crush` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0723_candy_crush` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0723_candy_crush` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0723_candy_crush` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0723_candy_crush` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0723_candy_crush` |

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
.\scripts\test.ps1 -Folder 0723_candy_crush -AllLanguages
```

```bash
./scripts/test.sh --folder 0723_candy_crush --all-languages
```

```zsh
./scripts/test.sh --folder 0723_candy_crush --all-languages
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
