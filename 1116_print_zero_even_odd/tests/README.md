# Test harness for 1116_print_zero_even_odd

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1116_print_zero_even_odd --language python
./scripts/test.sh --folder 1116_print_zero_even_odd --language javascript
./scripts/test.sh --folder 1116_print_zero_even_odd --language typescript
./scripts/test.sh --folder 1116_print_zero_even_odd --language java
./scripts/test.sh --folder 1116_print_zero_even_odd --language cpp
./scripts/test.sh --folder 1116_print_zero_even_odd --language c
./scripts/test.sh --folder 1116_print_zero_even_odd --language go
./scripts/test.sh --folder 1116_print_zero_even_odd --language rust
./scripts/test.sh --folder 1116_print_zero_even_odd --language kotlin
./scripts/test.sh --folder 1116_print_zero_even_odd --language swift
./scripts/test.sh --folder 1116_print_zero_even_odd --language ruby
./scripts/test.sh --folder 1116_print_zero_even_odd --language csharp
./scripts/test.sh --folder 1116_print_zero_even_odd --language scala
./scripts/test.sh --folder 1116_print_zero_even_odd --language php
./scripts/test.sh --folder 1116_print_zero_even_odd --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1116_print_zero_even_odd --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm java java 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm c c 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm go go 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm rust rust 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm swift swift 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm scala scala 1116_print_zero_even_odd
docker compose -f docker/docker-compose.yml run --rm php php 1116_print_zero_even_odd
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1116_print_zero_even_odd` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1116_print_zero_even_odd` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1116_print_zero_even_odd` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1116_print_zero_even_odd` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1116_print_zero_even_odd` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1116_print_zero_even_odd` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1116_print_zero_even_odd` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1116_print_zero_even_odd` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1116_print_zero_even_odd` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1116_print_zero_even_odd` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1116_print_zero_even_odd` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1116_print_zero_even_odd` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1116_print_zero_even_odd` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1116_print_zero_even_odd` |

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
.\scripts\test.ps1 -Folder 1116_print_zero_even_odd -AllLanguages
```

```bash
./scripts/test.sh --folder 1116_print_zero_even_odd --all-languages
```

```zsh
./scripts/test.sh --folder 1116_print_zero_even_odd --all-languages
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
