# Test harness for 0721_accounts_merge

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0721_accounts_merge -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0721_accounts_merge --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0721_accounts_merge --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0721_accounts_merge --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0721_accounts_merge --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0721_accounts_merge --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0721_accounts_merge --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0721_accounts_merge --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0721_accounts_merge --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0721_accounts_merge --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0721_accounts_merge --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0721_accounts_merge --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0721_accounts_merge --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0721_accounts_merge --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0721_accounts_merge --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0721_accounts_merge --language python
./scripts/test.sh --folder 0721_accounts_merge --language javascript
./scripts/test.sh --folder 0721_accounts_merge --language typescript
./scripts/test.sh --folder 0721_accounts_merge --language java
./scripts/test.sh --folder 0721_accounts_merge --language cpp
./scripts/test.sh --folder 0721_accounts_merge --language c
./scripts/test.sh --folder 0721_accounts_merge --language go
./scripts/test.sh --folder 0721_accounts_merge --language rust
./scripts/test.sh --folder 0721_accounts_merge --language kotlin
./scripts/test.sh --folder 0721_accounts_merge --language swift
./scripts/test.sh --folder 0721_accounts_merge --language ruby
./scripts/test.sh --folder 0721_accounts_merge --language csharp
./scripts/test.sh --folder 0721_accounts_merge --language scala
./scripts/test.sh --folder 0721_accounts_merge --language php
./scripts/test.sh --folder 0721_accounts_merge --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0721_accounts_merge --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0721_accounts_merge --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0721_accounts_merge --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0721_accounts_merge --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0721_accounts_merge --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0721_accounts_merge --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0721_accounts_merge --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0721_accounts_merge --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0721_accounts_merge --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0721_accounts_merge --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0721_accounts_merge --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0721_accounts_merge --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0721_accounts_merge --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0721_accounts_merge --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm java java 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm c c 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm go go 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm rust rust 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm swift swift 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm scala scala 0721_accounts_merge
docker compose -f docker/docker-compose.yml run --rm php php 0721_accounts_merge
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0721_accounts_merge` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0721_accounts_merge` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0721_accounts_merge` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0721_accounts_merge` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0721_accounts_merge` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0721_accounts_merge` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0721_accounts_merge` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0721_accounts_merge` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0721_accounts_merge` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0721_accounts_merge` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0721_accounts_merge` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0721_accounts_merge` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0721_accounts_merge` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0721_accounts_merge` |

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
.\scripts\test.ps1 -Folder 0721_accounts_merge -AllLanguages
```

```bash
./scripts/test.sh --folder 0721_accounts_merge --all-languages
```

```zsh
./scripts/test.sh --folder 0721_accounts_merge --all-languages
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
