# Test harness for 2784_check_if_array_is_good

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2784_check_if_array_is_good --language python
./scripts/test.sh --folder 2784_check_if_array_is_good --language javascript
./scripts/test.sh --folder 2784_check_if_array_is_good --language typescript
./scripts/test.sh --folder 2784_check_if_array_is_good --language java
./scripts/test.sh --folder 2784_check_if_array_is_good --language cpp
./scripts/test.sh --folder 2784_check_if_array_is_good --language c
./scripts/test.sh --folder 2784_check_if_array_is_good --language go
./scripts/test.sh --folder 2784_check_if_array_is_good --language rust
./scripts/test.sh --folder 2784_check_if_array_is_good --language kotlin
./scripts/test.sh --folder 2784_check_if_array_is_good --language swift
./scripts/test.sh --folder 2784_check_if_array_is_good --language ruby
./scripts/test.sh --folder 2784_check_if_array_is_good --language csharp
./scripts/test.sh --folder 2784_check_if_array_is_good --language scala
./scripts/test.sh --folder 2784_check_if_array_is_good --language php
./scripts/test.sh --folder 2784_check_if_array_is_good --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2784_check_if_array_is_good --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm java java 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm c c 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm go go 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm rust rust 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm swift swift 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm scala scala 2784_check_if_array_is_good
docker compose -f docker/docker-compose.yml run --rm php php 2784_check_if_array_is_good
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2784_check_if_array_is_good` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2784_check_if_array_is_good` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2784_check_if_array_is_good` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2784_check_if_array_is_good` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2784_check_if_array_is_good` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2784_check_if_array_is_good` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2784_check_if_array_is_good` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2784_check_if_array_is_good` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2784_check_if_array_is_good` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2784_check_if_array_is_good` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2784_check_if_array_is_good` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2784_check_if_array_is_good` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2784_check_if_array_is_good` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2784_check_if_array_is_good` |

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
.\scripts\test.ps1 -Folder 2784_check_if_array_is_good -AllLanguages
```

```bash
./scripts/test.sh --folder 2784_check_if_array_is_good --all-languages
```

```zsh
./scripts/test.sh --folder 2784_check_if_array_is_good --all-languages
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
