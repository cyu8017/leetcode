# Test harness for 0799_champagne_tower

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0799_champagne_tower -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0799_champagne_tower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0799_champagne_tower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0799_champagne_tower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0799_champagne_tower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0799_champagne_tower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0799_champagne_tower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0799_champagne_tower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0799_champagne_tower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0799_champagne_tower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0799_champagne_tower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0799_champagne_tower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0799_champagne_tower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0799_champagne_tower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0799_champagne_tower --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0799_champagne_tower --language python
./scripts/test.sh --folder 0799_champagne_tower --language javascript
./scripts/test.sh --folder 0799_champagne_tower --language typescript
./scripts/test.sh --folder 0799_champagne_tower --language java
./scripts/test.sh --folder 0799_champagne_tower --language cpp
./scripts/test.sh --folder 0799_champagne_tower --language c
./scripts/test.sh --folder 0799_champagne_tower --language go
./scripts/test.sh --folder 0799_champagne_tower --language rust
./scripts/test.sh --folder 0799_champagne_tower --language kotlin
./scripts/test.sh --folder 0799_champagne_tower --language swift
./scripts/test.sh --folder 0799_champagne_tower --language ruby
./scripts/test.sh --folder 0799_champagne_tower --language csharp
./scripts/test.sh --folder 0799_champagne_tower --language scala
./scripts/test.sh --folder 0799_champagne_tower --language php
./scripts/test.sh --folder 0799_champagne_tower --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0799_champagne_tower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0799_champagne_tower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0799_champagne_tower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0799_champagne_tower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0799_champagne_tower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0799_champagne_tower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0799_champagne_tower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0799_champagne_tower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0799_champagne_tower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0799_champagne_tower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0799_champagne_tower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0799_champagne_tower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0799_champagne_tower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0799_champagne_tower --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm java java 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm c c 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm go go 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm rust rust 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm swift swift 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm scala scala 0799_champagne_tower
docker compose -f docker/docker-compose.yml run --rm php php 0799_champagne_tower
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0799_champagne_tower` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0799_champagne_tower` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0799_champagne_tower` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0799_champagne_tower` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0799_champagne_tower` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0799_champagne_tower` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0799_champagne_tower` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0799_champagne_tower` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0799_champagne_tower` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0799_champagne_tower` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0799_champagne_tower` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0799_champagne_tower` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0799_champagne_tower` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0799_champagne_tower` |

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
.\scripts\test.ps1 -Folder 0799_champagne_tower -AllLanguages
```

```bash
./scripts/test.sh --folder 0799_champagne_tower --all-languages
```

```zsh
./scripts/test.sh --folder 0799_champagne_tower --all-languages
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
