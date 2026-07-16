# Test harness for 3433_count_mentions_per_user

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3433_count_mentions_per_user --language python
./scripts/test.sh --folder 3433_count_mentions_per_user --language javascript
./scripts/test.sh --folder 3433_count_mentions_per_user --language typescript
./scripts/test.sh --folder 3433_count_mentions_per_user --language java
./scripts/test.sh --folder 3433_count_mentions_per_user --language cpp
./scripts/test.sh --folder 3433_count_mentions_per_user --language c
./scripts/test.sh --folder 3433_count_mentions_per_user --language go
./scripts/test.sh --folder 3433_count_mentions_per_user --language rust
./scripts/test.sh --folder 3433_count_mentions_per_user --language kotlin
./scripts/test.sh --folder 3433_count_mentions_per_user --language swift
./scripts/test.sh --folder 3433_count_mentions_per_user --language ruby
./scripts/test.sh --folder 3433_count_mentions_per_user --language csharp
./scripts/test.sh --folder 3433_count_mentions_per_user --language scala
./scripts/test.sh --folder 3433_count_mentions_per_user --language php
./scripts/test.sh --folder 3433_count_mentions_per_user --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3433_count_mentions_per_user --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm java java 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm c c 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm go go 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm rust rust 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm swift swift 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm scala scala 3433_count_mentions_per_user
docker compose -f docker/docker-compose.yml run --rm php php 3433_count_mentions_per_user
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3433_count_mentions_per_user` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3433_count_mentions_per_user` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3433_count_mentions_per_user` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3433_count_mentions_per_user` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3433_count_mentions_per_user` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3433_count_mentions_per_user` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3433_count_mentions_per_user` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3433_count_mentions_per_user` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3433_count_mentions_per_user` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3433_count_mentions_per_user` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3433_count_mentions_per_user` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3433_count_mentions_per_user` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3433_count_mentions_per_user` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3433_count_mentions_per_user` |

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
.\scripts\test.ps1 -Folder 3433_count_mentions_per_user -AllLanguages
```

```bash
./scripts/test.sh --folder 3433_count_mentions_per_user --all-languages
```

```zsh
./scripts/test.sh --folder 3433_count_mentions_per_user --all-languages
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
