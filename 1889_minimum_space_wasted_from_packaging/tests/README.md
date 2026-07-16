# Test harness for 1889_minimum_space_wasted_from_packaging

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language python
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language javascript
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language typescript
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language java
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language cpp
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language c
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language go
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language rust
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language kotlin
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language swift
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language ruby
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language csharp
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language scala
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language php
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm java java 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm c c 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm go go 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm rust rust 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm swift swift 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm scala scala 1889_minimum_space_wasted_from_packaging
docker compose -f docker/docker-compose.yml run --rm php php 1889_minimum_space_wasted_from_packaging
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1889_minimum_space_wasted_from_packaging` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1889_minimum_space_wasted_from_packaging` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1889_minimum_space_wasted_from_packaging` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1889_minimum_space_wasted_from_packaging` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1889_minimum_space_wasted_from_packaging` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1889_minimum_space_wasted_from_packaging` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1889_minimum_space_wasted_from_packaging` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1889_minimum_space_wasted_from_packaging` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1889_minimum_space_wasted_from_packaging` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1889_minimum_space_wasted_from_packaging` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1889_minimum_space_wasted_from_packaging` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1889_minimum_space_wasted_from_packaging` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1889_minimum_space_wasted_from_packaging` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1889_minimum_space_wasted_from_packaging` |

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
.\scripts\test.ps1 -Folder 1889_minimum_space_wasted_from_packaging -AllLanguages
```

```bash
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --all-languages
```

```zsh
./scripts/test.sh --folder 1889_minimum_space_wasted_from_packaging --all-languages
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
