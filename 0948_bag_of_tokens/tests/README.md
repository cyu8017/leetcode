# Test harness for 0948_bag_of_tokens

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0948_bag_of_tokens -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0948_bag_of_tokens --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0948_bag_of_tokens --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0948_bag_of_tokens --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0948_bag_of_tokens --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0948_bag_of_tokens --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0948_bag_of_tokens --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0948_bag_of_tokens --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0948_bag_of_tokens --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0948_bag_of_tokens --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0948_bag_of_tokens --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0948_bag_of_tokens --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0948_bag_of_tokens --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0948_bag_of_tokens --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0948_bag_of_tokens --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0948_bag_of_tokens --language python
./scripts/test.sh --folder 0948_bag_of_tokens --language javascript
./scripts/test.sh --folder 0948_bag_of_tokens --language typescript
./scripts/test.sh --folder 0948_bag_of_tokens --language java
./scripts/test.sh --folder 0948_bag_of_tokens --language cpp
./scripts/test.sh --folder 0948_bag_of_tokens --language c
./scripts/test.sh --folder 0948_bag_of_tokens --language go
./scripts/test.sh --folder 0948_bag_of_tokens --language rust
./scripts/test.sh --folder 0948_bag_of_tokens --language kotlin
./scripts/test.sh --folder 0948_bag_of_tokens --language swift
./scripts/test.sh --folder 0948_bag_of_tokens --language ruby
./scripts/test.sh --folder 0948_bag_of_tokens --language csharp
./scripts/test.sh --folder 0948_bag_of_tokens --language scala
./scripts/test.sh --folder 0948_bag_of_tokens --language php
./scripts/test.sh --folder 0948_bag_of_tokens --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0948_bag_of_tokens --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0948_bag_of_tokens --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0948_bag_of_tokens --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0948_bag_of_tokens --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0948_bag_of_tokens --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0948_bag_of_tokens --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0948_bag_of_tokens --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0948_bag_of_tokens --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0948_bag_of_tokens --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0948_bag_of_tokens --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0948_bag_of_tokens --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0948_bag_of_tokens --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0948_bag_of_tokens --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0948_bag_of_tokens --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm java java 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm c c 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm go go 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm rust rust 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm swift swift 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm scala scala 0948_bag_of_tokens
docker compose -f docker/docker-compose.yml run --rm php php 0948_bag_of_tokens
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0948_bag_of_tokens` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0948_bag_of_tokens` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0948_bag_of_tokens` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0948_bag_of_tokens` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0948_bag_of_tokens` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0948_bag_of_tokens` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0948_bag_of_tokens` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0948_bag_of_tokens` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0948_bag_of_tokens` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0948_bag_of_tokens` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0948_bag_of_tokens` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0948_bag_of_tokens` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0948_bag_of_tokens` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0948_bag_of_tokens` |

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
.\scripts\test.ps1 -Folder 0948_bag_of_tokens -AllLanguages
```

```bash
./scripts/test.sh --folder 0948_bag_of_tokens --all-languages
```

```zsh
./scripts/test.sh --folder 0948_bag_of_tokens --all-languages
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
