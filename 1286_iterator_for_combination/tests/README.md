# Test harness for 1286_iterator_for_combination

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1286_iterator_for_combination -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1286_iterator_for_combination --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1286_iterator_for_combination --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1286_iterator_for_combination --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1286_iterator_for_combination --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1286_iterator_for_combination --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1286_iterator_for_combination --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1286_iterator_for_combination --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1286_iterator_for_combination --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1286_iterator_for_combination --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1286_iterator_for_combination --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1286_iterator_for_combination --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1286_iterator_for_combination --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1286_iterator_for_combination --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1286_iterator_for_combination --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1286_iterator_for_combination --language python
./scripts/test.sh --folder 1286_iterator_for_combination --language javascript
./scripts/test.sh --folder 1286_iterator_for_combination --language typescript
./scripts/test.sh --folder 1286_iterator_for_combination --language java
./scripts/test.sh --folder 1286_iterator_for_combination --language cpp
./scripts/test.sh --folder 1286_iterator_for_combination --language c
./scripts/test.sh --folder 1286_iterator_for_combination --language go
./scripts/test.sh --folder 1286_iterator_for_combination --language rust
./scripts/test.sh --folder 1286_iterator_for_combination --language kotlin
./scripts/test.sh --folder 1286_iterator_for_combination --language swift
./scripts/test.sh --folder 1286_iterator_for_combination --language ruby
./scripts/test.sh --folder 1286_iterator_for_combination --language csharp
./scripts/test.sh --folder 1286_iterator_for_combination --language scala
./scripts/test.sh --folder 1286_iterator_for_combination --language php
./scripts/test.sh --folder 1286_iterator_for_combination --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1286_iterator_for_combination --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1286_iterator_for_combination --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1286_iterator_for_combination --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1286_iterator_for_combination --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1286_iterator_for_combination --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1286_iterator_for_combination --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1286_iterator_for_combination --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1286_iterator_for_combination --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1286_iterator_for_combination --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1286_iterator_for_combination --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1286_iterator_for_combination --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1286_iterator_for_combination --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1286_iterator_for_combination --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1286_iterator_for_combination --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm java java 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm c c 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm go go 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm rust rust 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm swift swift 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm scala scala 1286_iterator_for_combination
docker compose -f docker/docker-compose.yml run --rm php php 1286_iterator_for_combination
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1286_iterator_for_combination` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1286_iterator_for_combination` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1286_iterator_for_combination` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1286_iterator_for_combination` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1286_iterator_for_combination` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1286_iterator_for_combination` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1286_iterator_for_combination` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1286_iterator_for_combination` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1286_iterator_for_combination` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1286_iterator_for_combination` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1286_iterator_for_combination` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1286_iterator_for_combination` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1286_iterator_for_combination` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1286_iterator_for_combination` |

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
.\scripts\test.ps1 -Folder 1286_iterator_for_combination -AllLanguages
```

```bash
./scripts/test.sh --folder 1286_iterator_for_combination --all-languages
```

```zsh
./scripts/test.sh --folder 1286_iterator_for_combination --all-languages
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
