# Test harness for 1762_buildings_with_an_ocean_view

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language python
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language javascript
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language typescript
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language java
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language cpp
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language c
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language go
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language rust
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language kotlin
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language swift
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language ruby
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language csharp
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language scala
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language php
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm java java 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm c c 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm go go 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm rust rust 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm swift swift 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm scala scala 1762_buildings_with_an_ocean_view
docker compose -f docker/docker-compose.yml run --rm php php 1762_buildings_with_an_ocean_view
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1762_buildings_with_an_ocean_view` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1762_buildings_with_an_ocean_view` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1762_buildings_with_an_ocean_view` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1762_buildings_with_an_ocean_view` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1762_buildings_with_an_ocean_view` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1762_buildings_with_an_ocean_view` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1762_buildings_with_an_ocean_view` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1762_buildings_with_an_ocean_view` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1762_buildings_with_an_ocean_view` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1762_buildings_with_an_ocean_view` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1762_buildings_with_an_ocean_view` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1762_buildings_with_an_ocean_view` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1762_buildings_with_an_ocean_view` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1762_buildings_with_an_ocean_view` |

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
.\scripts\test.ps1 -Folder 1762_buildings_with_an_ocean_view -AllLanguages
```

```bash
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --all-languages
```

```zsh
./scripts/test.sh --folder 1762_buildings_with_an_ocean_view --all-languages
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
