# Test harness for 1126_active_businesses

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1126_active_businesses -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1126_active_businesses --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1126_active_businesses --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1126_active_businesses --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1126_active_businesses --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1126_active_businesses --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1126_active_businesses --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1126_active_businesses --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1126_active_businesses --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1126_active_businesses --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1126_active_businesses --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1126_active_businesses --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1126_active_businesses --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1126_active_businesses --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1126_active_businesses --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1126_active_businesses --language python
./scripts/test.sh --folder 1126_active_businesses --language javascript
./scripts/test.sh --folder 1126_active_businesses --language typescript
./scripts/test.sh --folder 1126_active_businesses --language java
./scripts/test.sh --folder 1126_active_businesses --language cpp
./scripts/test.sh --folder 1126_active_businesses --language c
./scripts/test.sh --folder 1126_active_businesses --language go
./scripts/test.sh --folder 1126_active_businesses --language rust
./scripts/test.sh --folder 1126_active_businesses --language kotlin
./scripts/test.sh --folder 1126_active_businesses --language swift
./scripts/test.sh --folder 1126_active_businesses --language ruby
./scripts/test.sh --folder 1126_active_businesses --language csharp
./scripts/test.sh --folder 1126_active_businesses --language scala
./scripts/test.sh --folder 1126_active_businesses --language php
./scripts/test.sh --folder 1126_active_businesses --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1126_active_businesses --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1126_active_businesses --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1126_active_businesses --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1126_active_businesses --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1126_active_businesses --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1126_active_businesses --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1126_active_businesses --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1126_active_businesses --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1126_active_businesses --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1126_active_businesses --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1126_active_businesses --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1126_active_businesses --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1126_active_businesses --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1126_active_businesses --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm java java 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm c c 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm go go 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm rust rust 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm swift swift 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm scala scala 1126_active_businesses
docker compose -f docker/docker-compose.yml run --rm php php 1126_active_businesses
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1126_active_businesses` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1126_active_businesses` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1126_active_businesses` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1126_active_businesses` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1126_active_businesses` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1126_active_businesses` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1126_active_businesses` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1126_active_businesses` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1126_active_businesses` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1126_active_businesses` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1126_active_businesses` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1126_active_businesses` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1126_active_businesses` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1126_active_businesses` |

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
.\scripts\test.ps1 -Folder 1126_active_businesses -AllLanguages
```

```bash
./scripts/test.sh --folder 1126_active_businesses --all-languages
```

```zsh
./scripts/test.sh --folder 1126_active_businesses --all-languages
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
