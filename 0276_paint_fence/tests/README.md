# Test harness for 0276_paint_fence

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0276_paint_fence -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0276_paint_fence --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0276_paint_fence --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0276_paint_fence --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0276_paint_fence --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0276_paint_fence --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0276_paint_fence --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0276_paint_fence --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0276_paint_fence --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0276_paint_fence --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0276_paint_fence --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0276_paint_fence --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0276_paint_fence --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0276_paint_fence --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0276_paint_fence --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0276_paint_fence --language python
./scripts/test.sh --folder 0276_paint_fence --language javascript
./scripts/test.sh --folder 0276_paint_fence --language typescript
./scripts/test.sh --folder 0276_paint_fence --language java
./scripts/test.sh --folder 0276_paint_fence --language cpp
./scripts/test.sh --folder 0276_paint_fence --language c
./scripts/test.sh --folder 0276_paint_fence --language go
./scripts/test.sh --folder 0276_paint_fence --language rust
./scripts/test.sh --folder 0276_paint_fence --language kotlin
./scripts/test.sh --folder 0276_paint_fence --language swift
./scripts/test.sh --folder 0276_paint_fence --language ruby
./scripts/test.sh --folder 0276_paint_fence --language csharp
./scripts/test.sh --folder 0276_paint_fence --language scala
./scripts/test.sh --folder 0276_paint_fence --language php
./scripts/test.sh --folder 0276_paint_fence --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0276_paint_fence --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0276_paint_fence --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0276_paint_fence --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0276_paint_fence --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0276_paint_fence --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0276_paint_fence --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0276_paint_fence --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0276_paint_fence --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0276_paint_fence --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0276_paint_fence --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0276_paint_fence --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0276_paint_fence --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0276_paint_fence --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0276_paint_fence --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm java java 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm c c 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm go go 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm rust rust 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm swift swift 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm scala scala 0276_paint_fence
docker compose -f docker/docker-compose.yml run --rm php php 0276_paint_fence
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0276_paint_fence` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0276_paint_fence` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0276_paint_fence` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0276_paint_fence` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0276_paint_fence` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0276_paint_fence` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0276_paint_fence` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0276_paint_fence` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0276_paint_fence` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0276_paint_fence` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0276_paint_fence` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0276_paint_fence` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0276_paint_fence` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0276_paint_fence` |

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
.\scripts\test.ps1 -Folder 0276_paint_fence -AllLanguages
```

```bash
./scripts/test.sh --folder 0276_paint_fence --all-languages
```

```zsh
./scripts/test.sh --folder 0276_paint_fence --all-languages
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
