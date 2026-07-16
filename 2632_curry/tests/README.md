# Test harness for 2632_curry

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2632_curry -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2632_curry -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2632_curry -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2632_curry -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2632_curry -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2632_curry -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2632_curry -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2632_curry -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2632_curry -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2632_curry -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2632_curry -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2632_curry -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2632_curry -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2632_curry -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2632_curry --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2632_curry --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2632_curry --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2632_curry --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2632_curry --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2632_curry --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2632_curry --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2632_curry --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2632_curry --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2632_curry --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2632_curry --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2632_curry --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2632_curry --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2632_curry --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2632_curry --language python
./scripts/test.sh --folder 2632_curry --language javascript
./scripts/test.sh --folder 2632_curry --language typescript
./scripts/test.sh --folder 2632_curry --language java
./scripts/test.sh --folder 2632_curry --language cpp
./scripts/test.sh --folder 2632_curry --language c
./scripts/test.sh --folder 2632_curry --language go
./scripts/test.sh --folder 2632_curry --language rust
./scripts/test.sh --folder 2632_curry --language kotlin
./scripts/test.sh --folder 2632_curry --language swift
./scripts/test.sh --folder 2632_curry --language ruby
./scripts/test.sh --folder 2632_curry --language csharp
./scripts/test.sh --folder 2632_curry --language scala
./scripts/test.sh --folder 2632_curry --language php
./scripts/test.sh --folder 2632_curry --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2632_curry --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2632_curry --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2632_curry --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2632_curry --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2632_curry --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2632_curry --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2632_curry --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2632_curry --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2632_curry --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2632_curry --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2632_curry --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2632_curry --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2632_curry --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2632_curry --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2632_curry
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2632_curry
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2632_curry
docker compose -f docker/docker-compose.yml run --rm java java 2632_curry
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2632_curry
docker compose -f docker/docker-compose.yml run --rm c c 2632_curry
docker compose -f docker/docker-compose.yml run --rm go go 2632_curry
docker compose -f docker/docker-compose.yml run --rm rust rust 2632_curry
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2632_curry
docker compose -f docker/docker-compose.yml run --rm swift swift 2632_curry
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2632_curry
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2632_curry
docker compose -f docker/docker-compose.yml run --rm scala scala 2632_curry
docker compose -f docker/docker-compose.yml run --rm php php 2632_curry
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2632_curry` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2632_curry` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2632_curry` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2632_curry` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2632_curry` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2632_curry` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2632_curry` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2632_curry` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2632_curry` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2632_curry` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2632_curry` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2632_curry` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2632_curry` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2632_curry` |

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
.\scripts\test.ps1 -Folder 2632_curry -AllLanguages
```

```bash
./scripts/test.sh --folder 2632_curry --all-languages
```

```zsh
./scripts/test.sh --folder 2632_curry --all-languages
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
