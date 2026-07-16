# Test harness for 3866_first_unique_even_element

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3866_first_unique_even_element -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3866_first_unique_even_element --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3866_first_unique_even_element --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3866_first_unique_even_element --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3866_first_unique_even_element --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3866_first_unique_even_element --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3866_first_unique_even_element --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3866_first_unique_even_element --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3866_first_unique_even_element --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3866_first_unique_even_element --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3866_first_unique_even_element --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3866_first_unique_even_element --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3866_first_unique_even_element --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3866_first_unique_even_element --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3866_first_unique_even_element --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3866_first_unique_even_element --language python
./scripts/test.sh --folder 3866_first_unique_even_element --language javascript
./scripts/test.sh --folder 3866_first_unique_even_element --language typescript
./scripts/test.sh --folder 3866_first_unique_even_element --language java
./scripts/test.sh --folder 3866_first_unique_even_element --language cpp
./scripts/test.sh --folder 3866_first_unique_even_element --language c
./scripts/test.sh --folder 3866_first_unique_even_element --language go
./scripts/test.sh --folder 3866_first_unique_even_element --language rust
./scripts/test.sh --folder 3866_first_unique_even_element --language kotlin
./scripts/test.sh --folder 3866_first_unique_even_element --language swift
./scripts/test.sh --folder 3866_first_unique_even_element --language ruby
./scripts/test.sh --folder 3866_first_unique_even_element --language csharp
./scripts/test.sh --folder 3866_first_unique_even_element --language scala
./scripts/test.sh --folder 3866_first_unique_even_element --language php
./scripts/test.sh --folder 3866_first_unique_even_element --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3866_first_unique_even_element --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3866_first_unique_even_element --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3866_first_unique_even_element --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3866_first_unique_even_element --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3866_first_unique_even_element --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3866_first_unique_even_element --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3866_first_unique_even_element --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3866_first_unique_even_element --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3866_first_unique_even_element --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3866_first_unique_even_element --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3866_first_unique_even_element --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3866_first_unique_even_element --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3866_first_unique_even_element --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3866_first_unique_even_element --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm java java 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm c c 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm go go 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm rust rust 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm swift swift 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm scala scala 3866_first_unique_even_element
docker compose -f docker/docker-compose.yml run --rm php php 3866_first_unique_even_element
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3866_first_unique_even_element` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3866_first_unique_even_element` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3866_first_unique_even_element` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3866_first_unique_even_element` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3866_first_unique_even_element` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3866_first_unique_even_element` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3866_first_unique_even_element` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3866_first_unique_even_element` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3866_first_unique_even_element` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3866_first_unique_even_element` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3866_first_unique_even_element` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3866_first_unique_even_element` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3866_first_unique_even_element` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3866_first_unique_even_element` |

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
.\scripts\test.ps1 -Folder 3866_first_unique_even_element -AllLanguages
```

```bash
./scripts/test.sh --folder 3866_first_unique_even_element --all-languages
```

```zsh
./scripts/test.sh --folder 3866_first_unique_even_element --all-languages
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
