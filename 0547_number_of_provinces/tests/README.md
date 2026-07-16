# Test harness for 0547_number_of_provinces

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0547_number_of_provinces -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0547_number_of_provinces --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0547_number_of_provinces --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0547_number_of_provinces --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0547_number_of_provinces --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0547_number_of_provinces --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0547_number_of_provinces --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0547_number_of_provinces --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0547_number_of_provinces --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0547_number_of_provinces --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0547_number_of_provinces --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0547_number_of_provinces --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0547_number_of_provinces --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0547_number_of_provinces --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0547_number_of_provinces --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0547_number_of_provinces --language python
./scripts/test.sh --folder 0547_number_of_provinces --language javascript
./scripts/test.sh --folder 0547_number_of_provinces --language typescript
./scripts/test.sh --folder 0547_number_of_provinces --language java
./scripts/test.sh --folder 0547_number_of_provinces --language cpp
./scripts/test.sh --folder 0547_number_of_provinces --language c
./scripts/test.sh --folder 0547_number_of_provinces --language go
./scripts/test.sh --folder 0547_number_of_provinces --language rust
./scripts/test.sh --folder 0547_number_of_provinces --language kotlin
./scripts/test.sh --folder 0547_number_of_provinces --language swift
./scripts/test.sh --folder 0547_number_of_provinces --language ruby
./scripts/test.sh --folder 0547_number_of_provinces --language csharp
./scripts/test.sh --folder 0547_number_of_provinces --language scala
./scripts/test.sh --folder 0547_number_of_provinces --language php
./scripts/test.sh --folder 0547_number_of_provinces --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0547_number_of_provinces --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0547_number_of_provinces --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0547_number_of_provinces --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0547_number_of_provinces --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0547_number_of_provinces --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0547_number_of_provinces --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0547_number_of_provinces --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0547_number_of_provinces --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0547_number_of_provinces --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0547_number_of_provinces --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0547_number_of_provinces --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0547_number_of_provinces --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0547_number_of_provinces --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0547_number_of_provinces --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm java java 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm c c 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm go go 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm rust rust 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm swift swift 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm scala scala 0547_number_of_provinces
docker compose -f docker/docker-compose.yml run --rm php php 0547_number_of_provinces
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0547_number_of_provinces` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0547_number_of_provinces` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0547_number_of_provinces` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0547_number_of_provinces` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0547_number_of_provinces` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0547_number_of_provinces` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0547_number_of_provinces` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0547_number_of_provinces` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0547_number_of_provinces` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0547_number_of_provinces` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0547_number_of_provinces` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0547_number_of_provinces` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0547_number_of_provinces` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0547_number_of_provinces` |

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
.\scripts\test.ps1 -Folder 0547_number_of_provinces -AllLanguages
```

```bash
./scripts/test.sh --folder 0547_number_of_provinces --all-languages
```

```zsh
./scripts/test.sh --folder 0547_number_of_provinces --all-languages
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
