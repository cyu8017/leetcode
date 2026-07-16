# Test harness for 3332_maximum_points_tourist_can_earn

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language python
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language javascript
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language typescript
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language java
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language cpp
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language c
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language go
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language rust
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language kotlin
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language swift
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language ruby
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language csharp
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language scala
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language php
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm java java 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm c c 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm go go 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm rust rust 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm swift swift 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm scala scala 3332_maximum_points_tourist_can_earn
docker compose -f docker/docker-compose.yml run --rm php php 3332_maximum_points_tourist_can_earn
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3332_maximum_points_tourist_can_earn` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3332_maximum_points_tourist_can_earn` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3332_maximum_points_tourist_can_earn` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3332_maximum_points_tourist_can_earn` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3332_maximum_points_tourist_can_earn` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3332_maximum_points_tourist_can_earn` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3332_maximum_points_tourist_can_earn` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3332_maximum_points_tourist_can_earn` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3332_maximum_points_tourist_can_earn` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3332_maximum_points_tourist_can_earn` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3332_maximum_points_tourist_can_earn` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3332_maximum_points_tourist_can_earn` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3332_maximum_points_tourist_can_earn` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3332_maximum_points_tourist_can_earn` |

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
.\scripts\test.ps1 -Folder 3332_maximum_points_tourist_can_earn -AllLanguages
```

```bash
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --all-languages
```

```zsh
./scripts/test.sh --folder 3332_maximum_points_tourist_can_earn --all-languages
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
