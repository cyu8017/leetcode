# Test harness for 0651_4_keys_keyboard

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0651_4_keys_keyboard --language python
./scripts/test.sh --folder 0651_4_keys_keyboard --language javascript
./scripts/test.sh --folder 0651_4_keys_keyboard --language typescript
./scripts/test.sh --folder 0651_4_keys_keyboard --language java
./scripts/test.sh --folder 0651_4_keys_keyboard --language cpp
./scripts/test.sh --folder 0651_4_keys_keyboard --language c
./scripts/test.sh --folder 0651_4_keys_keyboard --language go
./scripts/test.sh --folder 0651_4_keys_keyboard --language rust
./scripts/test.sh --folder 0651_4_keys_keyboard --language kotlin
./scripts/test.sh --folder 0651_4_keys_keyboard --language swift
./scripts/test.sh --folder 0651_4_keys_keyboard --language ruby
./scripts/test.sh --folder 0651_4_keys_keyboard --language csharp
./scripts/test.sh --folder 0651_4_keys_keyboard --language scala
./scripts/test.sh --folder 0651_4_keys_keyboard --language php
./scripts/test.sh --folder 0651_4_keys_keyboard --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0651_4_keys_keyboard --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm java java 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm c c 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm go go 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm rust rust 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm swift swift 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm scala scala 0651_4_keys_keyboard
docker compose -f docker/docker-compose.yml run --rm php php 0651_4_keys_keyboard
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0651_4_keys_keyboard` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0651_4_keys_keyboard` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0651_4_keys_keyboard` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0651_4_keys_keyboard` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0651_4_keys_keyboard` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0651_4_keys_keyboard` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0651_4_keys_keyboard` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0651_4_keys_keyboard` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0651_4_keys_keyboard` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0651_4_keys_keyboard` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0651_4_keys_keyboard` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0651_4_keys_keyboard` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0651_4_keys_keyboard` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0651_4_keys_keyboard` |

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
.\scripts\test.ps1 -Folder 0651_4_keys_keyboard -AllLanguages
```

```bash
./scripts/test.sh --folder 0651_4_keys_keyboard --all-languages
```

```zsh
./scripts/test.sh --folder 0651_4_keys_keyboard --all-languages
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
