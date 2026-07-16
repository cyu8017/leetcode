# Test harness for 0969_pancake_sorting

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0969_pancake_sorting -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0969_pancake_sorting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0969_pancake_sorting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0969_pancake_sorting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0969_pancake_sorting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0969_pancake_sorting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0969_pancake_sorting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0969_pancake_sorting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0969_pancake_sorting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0969_pancake_sorting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0969_pancake_sorting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0969_pancake_sorting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0969_pancake_sorting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0969_pancake_sorting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0969_pancake_sorting --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0969_pancake_sorting --language python
./scripts/test.sh --folder 0969_pancake_sorting --language javascript
./scripts/test.sh --folder 0969_pancake_sorting --language typescript
./scripts/test.sh --folder 0969_pancake_sorting --language java
./scripts/test.sh --folder 0969_pancake_sorting --language cpp
./scripts/test.sh --folder 0969_pancake_sorting --language c
./scripts/test.sh --folder 0969_pancake_sorting --language go
./scripts/test.sh --folder 0969_pancake_sorting --language rust
./scripts/test.sh --folder 0969_pancake_sorting --language kotlin
./scripts/test.sh --folder 0969_pancake_sorting --language swift
./scripts/test.sh --folder 0969_pancake_sorting --language ruby
./scripts/test.sh --folder 0969_pancake_sorting --language csharp
./scripts/test.sh --folder 0969_pancake_sorting --language scala
./scripts/test.sh --folder 0969_pancake_sorting --language php
./scripts/test.sh --folder 0969_pancake_sorting --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0969_pancake_sorting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0969_pancake_sorting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0969_pancake_sorting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0969_pancake_sorting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0969_pancake_sorting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0969_pancake_sorting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0969_pancake_sorting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0969_pancake_sorting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0969_pancake_sorting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0969_pancake_sorting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0969_pancake_sorting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0969_pancake_sorting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0969_pancake_sorting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0969_pancake_sorting --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm java java 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm c c 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm go go 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm rust rust 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm swift swift 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm scala scala 0969_pancake_sorting
docker compose -f docker/docker-compose.yml run --rm php php 0969_pancake_sorting
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0969_pancake_sorting` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0969_pancake_sorting` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0969_pancake_sorting` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0969_pancake_sorting` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0969_pancake_sorting` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0969_pancake_sorting` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0969_pancake_sorting` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0969_pancake_sorting` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0969_pancake_sorting` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0969_pancake_sorting` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0969_pancake_sorting` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0969_pancake_sorting` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0969_pancake_sorting` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0969_pancake_sorting` |

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
.\scripts\test.ps1 -Folder 0969_pancake_sorting -AllLanguages
```

```bash
./scripts/test.sh --folder 0969_pancake_sorting --all-languages
```

```zsh
./scripts/test.sh --folder 0969_pancake_sorting --all-languages
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
