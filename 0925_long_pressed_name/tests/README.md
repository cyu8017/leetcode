# Test harness for 0925_long_pressed_name

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0925_long_pressed_name -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0925_long_pressed_name --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0925_long_pressed_name --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0925_long_pressed_name --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0925_long_pressed_name --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0925_long_pressed_name --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0925_long_pressed_name --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0925_long_pressed_name --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0925_long_pressed_name --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0925_long_pressed_name --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0925_long_pressed_name --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0925_long_pressed_name --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0925_long_pressed_name --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0925_long_pressed_name --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0925_long_pressed_name --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0925_long_pressed_name --language python
./scripts/test.sh --folder 0925_long_pressed_name --language javascript
./scripts/test.sh --folder 0925_long_pressed_name --language typescript
./scripts/test.sh --folder 0925_long_pressed_name --language java
./scripts/test.sh --folder 0925_long_pressed_name --language cpp
./scripts/test.sh --folder 0925_long_pressed_name --language c
./scripts/test.sh --folder 0925_long_pressed_name --language go
./scripts/test.sh --folder 0925_long_pressed_name --language rust
./scripts/test.sh --folder 0925_long_pressed_name --language kotlin
./scripts/test.sh --folder 0925_long_pressed_name --language swift
./scripts/test.sh --folder 0925_long_pressed_name --language ruby
./scripts/test.sh --folder 0925_long_pressed_name --language csharp
./scripts/test.sh --folder 0925_long_pressed_name --language scala
./scripts/test.sh --folder 0925_long_pressed_name --language php
./scripts/test.sh --folder 0925_long_pressed_name --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0925_long_pressed_name --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0925_long_pressed_name --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0925_long_pressed_name --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0925_long_pressed_name --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0925_long_pressed_name --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0925_long_pressed_name --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0925_long_pressed_name --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0925_long_pressed_name --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0925_long_pressed_name --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0925_long_pressed_name --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0925_long_pressed_name --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0925_long_pressed_name --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0925_long_pressed_name --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0925_long_pressed_name --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm java java 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm c c 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm go go 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm rust rust 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm swift swift 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm scala scala 0925_long_pressed_name
docker compose -f docker/docker-compose.yml run --rm php php 0925_long_pressed_name
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0925_long_pressed_name` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0925_long_pressed_name` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0925_long_pressed_name` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0925_long_pressed_name` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0925_long_pressed_name` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0925_long_pressed_name` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0925_long_pressed_name` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0925_long_pressed_name` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0925_long_pressed_name` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0925_long_pressed_name` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0925_long_pressed_name` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0925_long_pressed_name` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0925_long_pressed_name` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0925_long_pressed_name` |

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
.\scripts\test.ps1 -Folder 0925_long_pressed_name -AllLanguages
```

```bash
./scripts/test.sh --folder 0925_long_pressed_name --all-languages
```

```zsh
./scripts/test.sh --folder 0925_long_pressed_name --all-languages
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
