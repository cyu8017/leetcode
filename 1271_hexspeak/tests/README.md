# Test harness for 1271_hexspeak

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1271_hexspeak -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1271_hexspeak --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1271_hexspeak --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1271_hexspeak --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1271_hexspeak --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1271_hexspeak --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1271_hexspeak --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1271_hexspeak --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1271_hexspeak --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1271_hexspeak --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1271_hexspeak --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1271_hexspeak --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1271_hexspeak --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1271_hexspeak --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1271_hexspeak --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1271_hexspeak --language python
./scripts/test.sh --folder 1271_hexspeak --language javascript
./scripts/test.sh --folder 1271_hexspeak --language typescript
./scripts/test.sh --folder 1271_hexspeak --language java
./scripts/test.sh --folder 1271_hexspeak --language cpp
./scripts/test.sh --folder 1271_hexspeak --language c
./scripts/test.sh --folder 1271_hexspeak --language go
./scripts/test.sh --folder 1271_hexspeak --language rust
./scripts/test.sh --folder 1271_hexspeak --language kotlin
./scripts/test.sh --folder 1271_hexspeak --language swift
./scripts/test.sh --folder 1271_hexspeak --language ruby
./scripts/test.sh --folder 1271_hexspeak --language csharp
./scripts/test.sh --folder 1271_hexspeak --language scala
./scripts/test.sh --folder 1271_hexspeak --language php
./scripts/test.sh --folder 1271_hexspeak --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1271_hexspeak --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1271_hexspeak --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1271_hexspeak --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1271_hexspeak --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1271_hexspeak --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1271_hexspeak --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1271_hexspeak --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1271_hexspeak --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1271_hexspeak --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1271_hexspeak --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1271_hexspeak --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1271_hexspeak --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1271_hexspeak --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1271_hexspeak --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm java java 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm c c 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm go go 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm rust rust 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm swift swift 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm scala scala 1271_hexspeak
docker compose -f docker/docker-compose.yml run --rm php php 1271_hexspeak
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1271_hexspeak` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1271_hexspeak` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1271_hexspeak` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1271_hexspeak` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1271_hexspeak` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1271_hexspeak` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1271_hexspeak` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1271_hexspeak` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1271_hexspeak` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1271_hexspeak` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1271_hexspeak` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1271_hexspeak` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1271_hexspeak` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1271_hexspeak` |

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
.\scripts\test.ps1 -Folder 1271_hexspeak -AllLanguages
```

```bash
./scripts/test.sh --folder 1271_hexspeak --all-languages
```

```zsh
./scripts/test.sh --folder 1271_hexspeak --all-languages
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
