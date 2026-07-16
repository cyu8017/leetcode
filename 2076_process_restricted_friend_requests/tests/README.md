# Test harness for 2076_process_restricted_friend_requests

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language python
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language javascript
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language typescript
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language java
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language cpp
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language c
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language go
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language rust
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language kotlin
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language swift
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language ruby
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language csharp
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language scala
./scripts/test.sh --folder 2076_process_restricted_friend_requests --language php
./scripts/test.sh --folder 2076_process_restricted_friend_requests --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2076_process_restricted_friend_requests --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm java java 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm c c 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm go go 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm rust rust 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm swift swift 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm scala scala 2076_process_restricted_friend_requests
docker compose -f docker/docker-compose.yml run --rm php php 2076_process_restricted_friend_requests
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2076_process_restricted_friend_requests` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2076_process_restricted_friend_requests` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2076_process_restricted_friend_requests` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2076_process_restricted_friend_requests` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2076_process_restricted_friend_requests` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2076_process_restricted_friend_requests` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2076_process_restricted_friend_requests` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2076_process_restricted_friend_requests` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2076_process_restricted_friend_requests` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2076_process_restricted_friend_requests` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2076_process_restricted_friend_requests` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2076_process_restricted_friend_requests` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2076_process_restricted_friend_requests` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2076_process_restricted_friend_requests` |

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
.\scripts\test.ps1 -Folder 2076_process_restricted_friend_requests -AllLanguages
```

```bash
./scripts/test.sh --folder 2076_process_restricted_friend_requests --all-languages
```

```zsh
./scripts/test.sh --folder 2076_process_restricted_friend_requests --all-languages
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
