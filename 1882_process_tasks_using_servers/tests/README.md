# Test harness for 1882_process_tasks_using_servers

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1882_process_tasks_using_servers --language python
./scripts/test.sh --folder 1882_process_tasks_using_servers --language javascript
./scripts/test.sh --folder 1882_process_tasks_using_servers --language typescript
./scripts/test.sh --folder 1882_process_tasks_using_servers --language java
./scripts/test.sh --folder 1882_process_tasks_using_servers --language cpp
./scripts/test.sh --folder 1882_process_tasks_using_servers --language c
./scripts/test.sh --folder 1882_process_tasks_using_servers --language go
./scripts/test.sh --folder 1882_process_tasks_using_servers --language rust
./scripts/test.sh --folder 1882_process_tasks_using_servers --language kotlin
./scripts/test.sh --folder 1882_process_tasks_using_servers --language swift
./scripts/test.sh --folder 1882_process_tasks_using_servers --language ruby
./scripts/test.sh --folder 1882_process_tasks_using_servers --language csharp
./scripts/test.sh --folder 1882_process_tasks_using_servers --language scala
./scripts/test.sh --folder 1882_process_tasks_using_servers --language php
./scripts/test.sh --folder 1882_process_tasks_using_servers --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1882_process_tasks_using_servers --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm java java 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm c c 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm go go 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm rust rust 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm swift swift 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm scala scala 1882_process_tasks_using_servers
docker compose -f docker/docker-compose.yml run --rm php php 1882_process_tasks_using_servers
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1882_process_tasks_using_servers` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1882_process_tasks_using_servers` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1882_process_tasks_using_servers` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1882_process_tasks_using_servers` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1882_process_tasks_using_servers` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1882_process_tasks_using_servers` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1882_process_tasks_using_servers` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1882_process_tasks_using_servers` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1882_process_tasks_using_servers` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1882_process_tasks_using_servers` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1882_process_tasks_using_servers` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1882_process_tasks_using_servers` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1882_process_tasks_using_servers` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1882_process_tasks_using_servers` |

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
.\scripts\test.ps1 -Folder 1882_process_tasks_using_servers -AllLanguages
```

```bash
./scripts/test.sh --folder 1882_process_tasks_using_servers --all-languages
```

```zsh
./scripts/test.sh --folder 1882_process_tasks_using_servers --all-languages
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
