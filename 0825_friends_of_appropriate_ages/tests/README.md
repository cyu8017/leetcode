# Test harness for 0825_friends_of_appropriate_ages

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language python
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language javascript
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language typescript
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language java
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language cpp
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language c
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language go
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language rust
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language kotlin
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language swift
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language ruby
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language csharp
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language scala
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language php
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0825_friends_of_appropriate_ages --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm java java 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm c c 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm go go 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm rust rust 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm swift swift 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm scala scala 0825_friends_of_appropriate_ages
docker compose -f docker/docker-compose.yml run --rm php php 0825_friends_of_appropriate_ages
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0825_friends_of_appropriate_ages` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0825_friends_of_appropriate_ages` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0825_friends_of_appropriate_ages` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0825_friends_of_appropriate_ages` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0825_friends_of_appropriate_ages` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0825_friends_of_appropriate_ages` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0825_friends_of_appropriate_ages` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0825_friends_of_appropriate_ages` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0825_friends_of_appropriate_ages` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0825_friends_of_appropriate_ages` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0825_friends_of_appropriate_ages` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0825_friends_of_appropriate_ages` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0825_friends_of_appropriate_ages` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0825_friends_of_appropriate_ages` |

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
.\scripts\test.ps1 -Folder 0825_friends_of_appropriate_ages -AllLanguages
```

```bash
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --all-languages
```

```zsh
./scripts/test.sh --folder 0825_friends_of_appropriate_ages --all-languages
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
