# Test harness for 1054_distant_barcodes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1054_distant_barcodes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1054_distant_barcodes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1054_distant_barcodes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1054_distant_barcodes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1054_distant_barcodes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1054_distant_barcodes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1054_distant_barcodes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1054_distant_barcodes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1054_distant_barcodes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1054_distant_barcodes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1054_distant_barcodes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1054_distant_barcodes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1054_distant_barcodes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1054_distant_barcodes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1054_distant_barcodes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1054_distant_barcodes --language python
./scripts/test.sh --folder 1054_distant_barcodes --language javascript
./scripts/test.sh --folder 1054_distant_barcodes --language typescript
./scripts/test.sh --folder 1054_distant_barcodes --language java
./scripts/test.sh --folder 1054_distant_barcodes --language cpp
./scripts/test.sh --folder 1054_distant_barcodes --language c
./scripts/test.sh --folder 1054_distant_barcodes --language go
./scripts/test.sh --folder 1054_distant_barcodes --language rust
./scripts/test.sh --folder 1054_distant_barcodes --language kotlin
./scripts/test.sh --folder 1054_distant_barcodes --language swift
./scripts/test.sh --folder 1054_distant_barcodes --language ruby
./scripts/test.sh --folder 1054_distant_barcodes --language csharp
./scripts/test.sh --folder 1054_distant_barcodes --language scala
./scripts/test.sh --folder 1054_distant_barcodes --language php
./scripts/test.sh --folder 1054_distant_barcodes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1054_distant_barcodes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1054_distant_barcodes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1054_distant_barcodes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1054_distant_barcodes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1054_distant_barcodes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1054_distant_barcodes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1054_distant_barcodes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1054_distant_barcodes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1054_distant_barcodes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1054_distant_barcodes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1054_distant_barcodes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1054_distant_barcodes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1054_distant_barcodes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1054_distant_barcodes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm java java 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm c c 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm go go 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm rust rust 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm swift swift 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm scala scala 1054_distant_barcodes
docker compose -f docker/docker-compose.yml run --rm php php 1054_distant_barcodes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1054_distant_barcodes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1054_distant_barcodes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1054_distant_barcodes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1054_distant_barcodes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1054_distant_barcodes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1054_distant_barcodes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1054_distant_barcodes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1054_distant_barcodes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1054_distant_barcodes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1054_distant_barcodes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1054_distant_barcodes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1054_distant_barcodes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1054_distant_barcodes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1054_distant_barcodes` |

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
.\scripts\test.ps1 -Folder 1054_distant_barcodes -AllLanguages
```

```bash
./scripts/test.sh --folder 1054_distant_barcodes --all-languages
```

```zsh
./scripts/test.sh --folder 1054_distant_barcodes --all-languages
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
