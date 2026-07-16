# Test harness for 1264_page_recommendations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1264_page_recommendations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1264_page_recommendations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1264_page_recommendations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1264_page_recommendations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1264_page_recommendations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1264_page_recommendations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1264_page_recommendations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1264_page_recommendations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1264_page_recommendations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1264_page_recommendations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1264_page_recommendations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1264_page_recommendations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1264_page_recommendations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1264_page_recommendations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1264_page_recommendations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1264_page_recommendations --language python
./scripts/test.sh --folder 1264_page_recommendations --language javascript
./scripts/test.sh --folder 1264_page_recommendations --language typescript
./scripts/test.sh --folder 1264_page_recommendations --language java
./scripts/test.sh --folder 1264_page_recommendations --language cpp
./scripts/test.sh --folder 1264_page_recommendations --language c
./scripts/test.sh --folder 1264_page_recommendations --language go
./scripts/test.sh --folder 1264_page_recommendations --language rust
./scripts/test.sh --folder 1264_page_recommendations --language kotlin
./scripts/test.sh --folder 1264_page_recommendations --language swift
./scripts/test.sh --folder 1264_page_recommendations --language ruby
./scripts/test.sh --folder 1264_page_recommendations --language csharp
./scripts/test.sh --folder 1264_page_recommendations --language scala
./scripts/test.sh --folder 1264_page_recommendations --language php
./scripts/test.sh --folder 1264_page_recommendations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1264_page_recommendations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1264_page_recommendations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1264_page_recommendations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1264_page_recommendations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1264_page_recommendations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1264_page_recommendations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1264_page_recommendations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1264_page_recommendations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1264_page_recommendations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1264_page_recommendations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1264_page_recommendations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1264_page_recommendations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1264_page_recommendations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1264_page_recommendations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm java java 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm c c 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm go go 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm rust rust 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm swift swift 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm scala scala 1264_page_recommendations
docker compose -f docker/docker-compose.yml run --rm php php 1264_page_recommendations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1264_page_recommendations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1264_page_recommendations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1264_page_recommendations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1264_page_recommendations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1264_page_recommendations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1264_page_recommendations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1264_page_recommendations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1264_page_recommendations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1264_page_recommendations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1264_page_recommendations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1264_page_recommendations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1264_page_recommendations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1264_page_recommendations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1264_page_recommendations` |

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
.\scripts\test.ps1 -Folder 1264_page_recommendations -AllLanguages
```

```bash
./scripts/test.sh --folder 1264_page_recommendations --all-languages
```

```zsh
./scripts/test.sh --folder 1264_page_recommendations --all-languages
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
