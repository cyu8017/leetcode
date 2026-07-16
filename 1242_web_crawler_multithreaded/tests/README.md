# Test harness for 1242_web_crawler_multithreaded

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language python
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language javascript
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language typescript
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language java
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language cpp
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language c
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language go
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language rust
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language kotlin
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language swift
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language ruby
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language csharp
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language scala
./scripts/test.sh --folder 1242_web_crawler_multithreaded --language php
./scripts/test.sh --folder 1242_web_crawler_multithreaded --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1242_web_crawler_multithreaded --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm java java 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm c c 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm go go 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm rust rust 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm swift swift 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm scala scala 1242_web_crawler_multithreaded
docker compose -f docker/docker-compose.yml run --rm php php 1242_web_crawler_multithreaded
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1242_web_crawler_multithreaded` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1242_web_crawler_multithreaded` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1242_web_crawler_multithreaded` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1242_web_crawler_multithreaded` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1242_web_crawler_multithreaded` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1242_web_crawler_multithreaded` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1242_web_crawler_multithreaded` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1242_web_crawler_multithreaded` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1242_web_crawler_multithreaded` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1242_web_crawler_multithreaded` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1242_web_crawler_multithreaded` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1242_web_crawler_multithreaded` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1242_web_crawler_multithreaded` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1242_web_crawler_multithreaded` |

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
.\scripts\test.ps1 -Folder 1242_web_crawler_multithreaded -AllLanguages
```

```bash
./scripts/test.sh --folder 1242_web_crawler_multithreaded --all-languages
```

```zsh
./scripts/test.sh --folder 1242_web_crawler_multithreaded --all-languages
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
