# Test harness for 2532_time_to_cross_a_bridge

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language python
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language javascript
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language typescript
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language java
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language cpp
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language c
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language go
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language rust
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language kotlin
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language swift
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language ruby
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language csharp
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language scala
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language php
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2532_time_to_cross_a_bridge --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm java java 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm c c 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm go go 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm rust rust 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm swift swift 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm scala scala 2532_time_to_cross_a_bridge
docker compose -f docker/docker-compose.yml run --rm php php 2532_time_to_cross_a_bridge
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2532_time_to_cross_a_bridge` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2532_time_to_cross_a_bridge` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2532_time_to_cross_a_bridge` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2532_time_to_cross_a_bridge` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2532_time_to_cross_a_bridge` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2532_time_to_cross_a_bridge` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2532_time_to_cross_a_bridge` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2532_time_to_cross_a_bridge` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2532_time_to_cross_a_bridge` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2532_time_to_cross_a_bridge` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2532_time_to_cross_a_bridge` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2532_time_to_cross_a_bridge` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2532_time_to_cross_a_bridge` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2532_time_to_cross_a_bridge` |

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
.\scripts\test.ps1 -Folder 2532_time_to_cross_a_bridge -AllLanguages
```

```bash
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --all-languages
```

```zsh
./scripts/test.sh --folder 2532_time_to_cross_a_bridge --all-languages
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
