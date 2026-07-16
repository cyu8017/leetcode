# Test harness for 1087_brace_expansion

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1087_brace_expansion -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1087_brace_expansion --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1087_brace_expansion --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1087_brace_expansion --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1087_brace_expansion --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1087_brace_expansion --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1087_brace_expansion --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1087_brace_expansion --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1087_brace_expansion --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1087_brace_expansion --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1087_brace_expansion --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1087_brace_expansion --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1087_brace_expansion --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1087_brace_expansion --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1087_brace_expansion --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1087_brace_expansion --language python
./scripts/test.sh --folder 1087_brace_expansion --language javascript
./scripts/test.sh --folder 1087_brace_expansion --language typescript
./scripts/test.sh --folder 1087_brace_expansion --language java
./scripts/test.sh --folder 1087_brace_expansion --language cpp
./scripts/test.sh --folder 1087_brace_expansion --language c
./scripts/test.sh --folder 1087_brace_expansion --language go
./scripts/test.sh --folder 1087_brace_expansion --language rust
./scripts/test.sh --folder 1087_brace_expansion --language kotlin
./scripts/test.sh --folder 1087_brace_expansion --language swift
./scripts/test.sh --folder 1087_brace_expansion --language ruby
./scripts/test.sh --folder 1087_brace_expansion --language csharp
./scripts/test.sh --folder 1087_brace_expansion --language scala
./scripts/test.sh --folder 1087_brace_expansion --language php
./scripts/test.sh --folder 1087_brace_expansion --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1087_brace_expansion --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1087_brace_expansion --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1087_brace_expansion --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1087_brace_expansion --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1087_brace_expansion --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1087_brace_expansion --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1087_brace_expansion --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1087_brace_expansion --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1087_brace_expansion --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1087_brace_expansion --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1087_brace_expansion --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1087_brace_expansion --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1087_brace_expansion --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1087_brace_expansion --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm java java 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm c c 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm go go 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm rust rust 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm swift swift 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm scala scala 1087_brace_expansion
docker compose -f docker/docker-compose.yml run --rm php php 1087_brace_expansion
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1087_brace_expansion` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1087_brace_expansion` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1087_brace_expansion` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1087_brace_expansion` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1087_brace_expansion` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1087_brace_expansion` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1087_brace_expansion` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1087_brace_expansion` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1087_brace_expansion` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1087_brace_expansion` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1087_brace_expansion` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1087_brace_expansion` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1087_brace_expansion` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1087_brace_expansion` |

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
.\scripts\test.ps1 -Folder 1087_brace_expansion -AllLanguages
```

```bash
./scripts/test.sh --folder 1087_brace_expansion --all-languages
```

```zsh
./scripts/test.sh --folder 1087_brace_expansion --all-languages
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
