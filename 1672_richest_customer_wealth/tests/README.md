# Test harness for 1672_richest_customer_wealth

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1672_richest_customer_wealth --language python
./scripts/test.sh --folder 1672_richest_customer_wealth --language javascript
./scripts/test.sh --folder 1672_richest_customer_wealth --language typescript
./scripts/test.sh --folder 1672_richest_customer_wealth --language java
./scripts/test.sh --folder 1672_richest_customer_wealth --language cpp
./scripts/test.sh --folder 1672_richest_customer_wealth --language c
./scripts/test.sh --folder 1672_richest_customer_wealth --language go
./scripts/test.sh --folder 1672_richest_customer_wealth --language rust
./scripts/test.sh --folder 1672_richest_customer_wealth --language kotlin
./scripts/test.sh --folder 1672_richest_customer_wealth --language swift
./scripts/test.sh --folder 1672_richest_customer_wealth --language ruby
./scripts/test.sh --folder 1672_richest_customer_wealth --language csharp
./scripts/test.sh --folder 1672_richest_customer_wealth --language scala
./scripts/test.sh --folder 1672_richest_customer_wealth --language php
./scripts/test.sh --folder 1672_richest_customer_wealth --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1672_richest_customer_wealth --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm java java 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm c c 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm go go 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm rust rust 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm swift swift 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm scala scala 1672_richest_customer_wealth
docker compose -f docker/docker-compose.yml run --rm php php 1672_richest_customer_wealth
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1672_richest_customer_wealth` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1672_richest_customer_wealth` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1672_richest_customer_wealth` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1672_richest_customer_wealth` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1672_richest_customer_wealth` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1672_richest_customer_wealth` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1672_richest_customer_wealth` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1672_richest_customer_wealth` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1672_richest_customer_wealth` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1672_richest_customer_wealth` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1672_richest_customer_wealth` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1672_richest_customer_wealth` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1672_richest_customer_wealth` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1672_richest_customer_wealth` |

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
.\scripts\test.ps1 -Folder 1672_richest_customer_wealth -AllLanguages
```

```bash
./scripts/test.sh --folder 1672_richest_customer_wealth --all-languages
```

```zsh
./scripts/test.sh --folder 1672_richest_customer_wealth --all-languages
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
