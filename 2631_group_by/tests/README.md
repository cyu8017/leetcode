# Test harness for 2631_group_by

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2631_group_by -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2631_group_by -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2631_group_by -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2631_group_by -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2631_group_by -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2631_group_by -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2631_group_by -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2631_group_by -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2631_group_by -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2631_group_by -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2631_group_by -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2631_group_by -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2631_group_by -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2631_group_by -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2631_group_by --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2631_group_by --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2631_group_by --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2631_group_by --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2631_group_by --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2631_group_by --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2631_group_by --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2631_group_by --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2631_group_by --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2631_group_by --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2631_group_by --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2631_group_by --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2631_group_by --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2631_group_by --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2631_group_by --language python
./scripts/test.sh --folder 2631_group_by --language javascript
./scripts/test.sh --folder 2631_group_by --language typescript
./scripts/test.sh --folder 2631_group_by --language java
./scripts/test.sh --folder 2631_group_by --language cpp
./scripts/test.sh --folder 2631_group_by --language c
./scripts/test.sh --folder 2631_group_by --language go
./scripts/test.sh --folder 2631_group_by --language rust
./scripts/test.sh --folder 2631_group_by --language kotlin
./scripts/test.sh --folder 2631_group_by --language swift
./scripts/test.sh --folder 2631_group_by --language ruby
./scripts/test.sh --folder 2631_group_by --language csharp
./scripts/test.sh --folder 2631_group_by --language scala
./scripts/test.sh --folder 2631_group_by --language php
./scripts/test.sh --folder 2631_group_by --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2631_group_by --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2631_group_by --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2631_group_by --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2631_group_by --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2631_group_by --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2631_group_by --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2631_group_by --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2631_group_by --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2631_group_by --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2631_group_by --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2631_group_by --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2631_group_by --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2631_group_by --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2631_group_by --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2631_group_by
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2631_group_by
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2631_group_by
docker compose -f docker/docker-compose.yml run --rm java java 2631_group_by
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2631_group_by
docker compose -f docker/docker-compose.yml run --rm c c 2631_group_by
docker compose -f docker/docker-compose.yml run --rm go go 2631_group_by
docker compose -f docker/docker-compose.yml run --rm rust rust 2631_group_by
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2631_group_by
docker compose -f docker/docker-compose.yml run --rm swift swift 2631_group_by
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2631_group_by
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2631_group_by
docker compose -f docker/docker-compose.yml run --rm scala scala 2631_group_by
docker compose -f docker/docker-compose.yml run --rm php php 2631_group_by
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2631_group_by` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2631_group_by` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2631_group_by` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2631_group_by` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2631_group_by` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2631_group_by` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2631_group_by` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2631_group_by` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2631_group_by` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2631_group_by` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2631_group_by` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2631_group_by` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2631_group_by` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2631_group_by` |

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
.\scripts\test.ps1 -Folder 2631_group_by -AllLanguages
```

```bash
./scripts/test.sh --folder 2631_group_by --all-languages
```

```zsh
./scripts/test.sh --folder 2631_group_by --all-languages
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
