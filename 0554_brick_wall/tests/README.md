# Test harness for 0554_brick_wall

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0554_brick_wall -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0554_brick_wall --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0554_brick_wall --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0554_brick_wall --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0554_brick_wall --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0554_brick_wall --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0554_brick_wall --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0554_brick_wall --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0554_brick_wall --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0554_brick_wall --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0554_brick_wall --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0554_brick_wall --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0554_brick_wall --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0554_brick_wall --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0554_brick_wall --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0554_brick_wall --language python
./scripts/test.sh --folder 0554_brick_wall --language javascript
./scripts/test.sh --folder 0554_brick_wall --language typescript
./scripts/test.sh --folder 0554_brick_wall --language java
./scripts/test.sh --folder 0554_brick_wall --language cpp
./scripts/test.sh --folder 0554_brick_wall --language c
./scripts/test.sh --folder 0554_brick_wall --language go
./scripts/test.sh --folder 0554_brick_wall --language rust
./scripts/test.sh --folder 0554_brick_wall --language kotlin
./scripts/test.sh --folder 0554_brick_wall --language swift
./scripts/test.sh --folder 0554_brick_wall --language ruby
./scripts/test.sh --folder 0554_brick_wall --language csharp
./scripts/test.sh --folder 0554_brick_wall --language scala
./scripts/test.sh --folder 0554_brick_wall --language php
./scripts/test.sh --folder 0554_brick_wall --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0554_brick_wall --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0554_brick_wall --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0554_brick_wall --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0554_brick_wall --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0554_brick_wall --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0554_brick_wall --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0554_brick_wall --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0554_brick_wall --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0554_brick_wall --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0554_brick_wall --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0554_brick_wall --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0554_brick_wall --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0554_brick_wall --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0554_brick_wall --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm java java 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm c c 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm go go 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm rust rust 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm swift swift 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm scala scala 0554_brick_wall
docker compose -f docker/docker-compose.yml run --rm php php 0554_brick_wall
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0554_brick_wall` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0554_brick_wall` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0554_brick_wall` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0554_brick_wall` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0554_brick_wall` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0554_brick_wall` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0554_brick_wall` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0554_brick_wall` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0554_brick_wall` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0554_brick_wall` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0554_brick_wall` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0554_brick_wall` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0554_brick_wall` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0554_brick_wall` |

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
.\scripts\test.ps1 -Folder 0554_brick_wall -AllLanguages
```

```bash
./scripts/test.sh --folder 0554_brick_wall --all-languages
```

```zsh
./scripts/test.sh --folder 0554_brick_wall --all-languages
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
