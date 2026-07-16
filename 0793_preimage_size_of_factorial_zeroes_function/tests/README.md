# Test harness for 0793_preimage_size_of_factorial_zeroes_function

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language python
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language javascript
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language typescript
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language java
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language cpp
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language c
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language go
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language rust
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language kotlin
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language swift
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language ruby
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language csharp
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language scala
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language php
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm java java 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm c c 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm go go 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm rust rust 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm swift swift 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm scala scala 0793_preimage_size_of_factorial_zeroes_function
docker compose -f docker/docker-compose.yml run --rm php php 0793_preimage_size_of_factorial_zeroes_function
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0793_preimage_size_of_factorial_zeroes_function` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0793_preimage_size_of_factorial_zeroes_function` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0793_preimage_size_of_factorial_zeroes_function` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0793_preimage_size_of_factorial_zeroes_function` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0793_preimage_size_of_factorial_zeroes_function` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0793_preimage_size_of_factorial_zeroes_function` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0793_preimage_size_of_factorial_zeroes_function` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0793_preimage_size_of_factorial_zeroes_function` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0793_preimage_size_of_factorial_zeroes_function` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0793_preimage_size_of_factorial_zeroes_function` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0793_preimage_size_of_factorial_zeroes_function` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0793_preimage_size_of_factorial_zeroes_function` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0793_preimage_size_of_factorial_zeroes_function` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0793_preimage_size_of_factorial_zeroes_function` |

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
.\scripts\test.ps1 -Folder 0793_preimage_size_of_factorial_zeroes_function -AllLanguages
```

```bash
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --all-languages
```

```zsh
./scripts/test.sh --folder 0793_preimage_size_of_factorial_zeroes_function --all-languages
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
