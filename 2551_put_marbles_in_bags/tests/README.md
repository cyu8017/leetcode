# Test harness for 2551_put_marbles_in_bags

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2551_put_marbles_in_bags --language python
./scripts/test.sh --folder 2551_put_marbles_in_bags --language javascript
./scripts/test.sh --folder 2551_put_marbles_in_bags --language typescript
./scripts/test.sh --folder 2551_put_marbles_in_bags --language java
./scripts/test.sh --folder 2551_put_marbles_in_bags --language cpp
./scripts/test.sh --folder 2551_put_marbles_in_bags --language c
./scripts/test.sh --folder 2551_put_marbles_in_bags --language go
./scripts/test.sh --folder 2551_put_marbles_in_bags --language rust
./scripts/test.sh --folder 2551_put_marbles_in_bags --language kotlin
./scripts/test.sh --folder 2551_put_marbles_in_bags --language swift
./scripts/test.sh --folder 2551_put_marbles_in_bags --language ruby
./scripts/test.sh --folder 2551_put_marbles_in_bags --language csharp
./scripts/test.sh --folder 2551_put_marbles_in_bags --language scala
./scripts/test.sh --folder 2551_put_marbles_in_bags --language php
./scripts/test.sh --folder 2551_put_marbles_in_bags --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2551_put_marbles_in_bags --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm java java 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm c c 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm go go 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm rust rust 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm swift swift 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm scala scala 2551_put_marbles_in_bags
docker compose -f docker/docker-compose.yml run --rm php php 2551_put_marbles_in_bags
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2551_put_marbles_in_bags` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2551_put_marbles_in_bags` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2551_put_marbles_in_bags` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2551_put_marbles_in_bags` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2551_put_marbles_in_bags` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2551_put_marbles_in_bags` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2551_put_marbles_in_bags` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2551_put_marbles_in_bags` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2551_put_marbles_in_bags` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2551_put_marbles_in_bags` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2551_put_marbles_in_bags` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2551_put_marbles_in_bags` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2551_put_marbles_in_bags` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2551_put_marbles_in_bags` |

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
.\scripts\test.ps1 -Folder 2551_put_marbles_in_bags -AllLanguages
```

```bash
./scripts/test.sh --folder 2551_put_marbles_in_bags --all-languages
```

```zsh
./scripts/test.sh --folder 2551_put_marbles_in_bags --all-languages
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
