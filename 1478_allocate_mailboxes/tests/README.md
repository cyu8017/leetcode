# Test harness for 1478_allocate_mailboxes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1478_allocate_mailboxes --language python
./scripts/test.sh --folder 1478_allocate_mailboxes --language javascript
./scripts/test.sh --folder 1478_allocate_mailboxes --language typescript
./scripts/test.sh --folder 1478_allocate_mailboxes --language java
./scripts/test.sh --folder 1478_allocate_mailboxes --language cpp
./scripts/test.sh --folder 1478_allocate_mailboxes --language c
./scripts/test.sh --folder 1478_allocate_mailboxes --language go
./scripts/test.sh --folder 1478_allocate_mailboxes --language rust
./scripts/test.sh --folder 1478_allocate_mailboxes --language kotlin
./scripts/test.sh --folder 1478_allocate_mailboxes --language swift
./scripts/test.sh --folder 1478_allocate_mailboxes --language ruby
./scripts/test.sh --folder 1478_allocate_mailboxes --language csharp
./scripts/test.sh --folder 1478_allocate_mailboxes --language scala
./scripts/test.sh --folder 1478_allocate_mailboxes --language php
./scripts/test.sh --folder 1478_allocate_mailboxes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1478_allocate_mailboxes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm java java 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm c c 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm go go 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm rust rust 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm swift swift 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm scala scala 1478_allocate_mailboxes
docker compose -f docker/docker-compose.yml run --rm php php 1478_allocate_mailboxes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1478_allocate_mailboxes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1478_allocate_mailboxes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1478_allocate_mailboxes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1478_allocate_mailboxes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1478_allocate_mailboxes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1478_allocate_mailboxes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1478_allocate_mailboxes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1478_allocate_mailboxes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1478_allocate_mailboxes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1478_allocate_mailboxes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1478_allocate_mailboxes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1478_allocate_mailboxes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1478_allocate_mailboxes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1478_allocate_mailboxes` |

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
.\scripts\test.ps1 -Folder 1478_allocate_mailboxes -AllLanguages
```

```bash
./scripts/test.sh --folder 1478_allocate_mailboxes --all-languages
```

```zsh
./scripts/test.sh --folder 1478_allocate_mailboxes --all-languages
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
