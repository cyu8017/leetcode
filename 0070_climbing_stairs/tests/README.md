# Test harness for 0070_climbing_stairs

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0070_climbing_stairs -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0070_climbing_stairs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0070_climbing_stairs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0070_climbing_stairs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0070_climbing_stairs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0070_climbing_stairs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0070_climbing_stairs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0070_climbing_stairs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0070_climbing_stairs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0070_climbing_stairs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0070_climbing_stairs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0070_climbing_stairs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0070_climbing_stairs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0070_climbing_stairs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0070_climbing_stairs --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0070_climbing_stairs --language python
./scripts/test.sh --folder 0070_climbing_stairs --language javascript
./scripts/test.sh --folder 0070_climbing_stairs --language typescript
./scripts/test.sh --folder 0070_climbing_stairs --language java
./scripts/test.sh --folder 0070_climbing_stairs --language cpp
./scripts/test.sh --folder 0070_climbing_stairs --language c
./scripts/test.sh --folder 0070_climbing_stairs --language go
./scripts/test.sh --folder 0070_climbing_stairs --language rust
./scripts/test.sh --folder 0070_climbing_stairs --language kotlin
./scripts/test.sh --folder 0070_climbing_stairs --language swift
./scripts/test.sh --folder 0070_climbing_stairs --language ruby
./scripts/test.sh --folder 0070_climbing_stairs --language csharp
./scripts/test.sh --folder 0070_climbing_stairs --language scala
./scripts/test.sh --folder 0070_climbing_stairs --language php
./scripts/test.sh --folder 0070_climbing_stairs --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0070_climbing_stairs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0070_climbing_stairs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0070_climbing_stairs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0070_climbing_stairs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0070_climbing_stairs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0070_climbing_stairs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0070_climbing_stairs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0070_climbing_stairs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0070_climbing_stairs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0070_climbing_stairs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0070_climbing_stairs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0070_climbing_stairs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0070_climbing_stairs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0070_climbing_stairs --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm java java 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm c c 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm go go 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm rust rust 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm swift swift 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm scala scala 0070_climbing_stairs
docker compose -f docker/docker-compose.yml run --rm php php 0070_climbing_stairs
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0070_climbing_stairs` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0070_climbing_stairs` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0070_climbing_stairs` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0070_climbing_stairs` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0070_climbing_stairs` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0070_climbing_stairs` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0070_climbing_stairs` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0070_climbing_stairs` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0070_climbing_stairs` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0070_climbing_stairs` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0070_climbing_stairs` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0070_climbing_stairs` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0070_climbing_stairs` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0070_climbing_stairs` |

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
.\scripts\test.ps1 -Folder 0070_climbing_stairs -AllLanguages
```

```bash
./scripts/test.sh --folder 0070_climbing_stairs --all-languages
```

```zsh
./scripts/test.sh --folder 0070_climbing_stairs --all-languages
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
