# Test harness for 0817_linked_list_components

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0817_linked_list_components -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0817_linked_list_components --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0817_linked_list_components --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0817_linked_list_components --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0817_linked_list_components --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0817_linked_list_components --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0817_linked_list_components --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0817_linked_list_components --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0817_linked_list_components --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0817_linked_list_components --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0817_linked_list_components --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0817_linked_list_components --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0817_linked_list_components --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0817_linked_list_components --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0817_linked_list_components --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0817_linked_list_components --language python
./scripts/test.sh --folder 0817_linked_list_components --language javascript
./scripts/test.sh --folder 0817_linked_list_components --language typescript
./scripts/test.sh --folder 0817_linked_list_components --language java
./scripts/test.sh --folder 0817_linked_list_components --language cpp
./scripts/test.sh --folder 0817_linked_list_components --language c
./scripts/test.sh --folder 0817_linked_list_components --language go
./scripts/test.sh --folder 0817_linked_list_components --language rust
./scripts/test.sh --folder 0817_linked_list_components --language kotlin
./scripts/test.sh --folder 0817_linked_list_components --language swift
./scripts/test.sh --folder 0817_linked_list_components --language ruby
./scripts/test.sh --folder 0817_linked_list_components --language csharp
./scripts/test.sh --folder 0817_linked_list_components --language scala
./scripts/test.sh --folder 0817_linked_list_components --language php
./scripts/test.sh --folder 0817_linked_list_components --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0817_linked_list_components --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0817_linked_list_components --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0817_linked_list_components --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0817_linked_list_components --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0817_linked_list_components --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0817_linked_list_components --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0817_linked_list_components --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0817_linked_list_components --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0817_linked_list_components --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0817_linked_list_components --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0817_linked_list_components --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0817_linked_list_components --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0817_linked_list_components --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0817_linked_list_components --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm java java 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm c c 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm go go 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm rust rust 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm swift swift 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm scala scala 0817_linked_list_components
docker compose -f docker/docker-compose.yml run --rm php php 0817_linked_list_components
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0817_linked_list_components` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0817_linked_list_components` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0817_linked_list_components` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0817_linked_list_components` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0817_linked_list_components` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0817_linked_list_components` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0817_linked_list_components` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0817_linked_list_components` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0817_linked_list_components` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0817_linked_list_components` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0817_linked_list_components` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0817_linked_list_components` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0817_linked_list_components` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0817_linked_list_components` |

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
.\scripts\test.ps1 -Folder 0817_linked_list_components -AllLanguages
```

```bash
./scripts/test.sh --folder 0817_linked_list_components --all-languages
```

```zsh
./scripts/test.sh --folder 0817_linked_list_components --all-languages
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
