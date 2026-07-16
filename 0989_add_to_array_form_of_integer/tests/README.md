# Test harness for 0989_add_to_array_form_of_integer

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language python
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language javascript
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language typescript
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language java
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language cpp
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language c
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language go
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language rust
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language kotlin
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language swift
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language ruby
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language csharp
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language scala
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language php
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0989_add_to_array_form_of_integer --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm java java 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm c c 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm go go 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm rust rust 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm swift swift 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm scala scala 0989_add_to_array_form_of_integer
docker compose -f docker/docker-compose.yml run --rm php php 0989_add_to_array_form_of_integer
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0989_add_to_array_form_of_integer` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0989_add_to_array_form_of_integer` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0989_add_to_array_form_of_integer` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0989_add_to_array_form_of_integer` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0989_add_to_array_form_of_integer` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0989_add_to_array_form_of_integer` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0989_add_to_array_form_of_integer` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0989_add_to_array_form_of_integer` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0989_add_to_array_form_of_integer` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0989_add_to_array_form_of_integer` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0989_add_to_array_form_of_integer` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0989_add_to_array_form_of_integer` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0989_add_to_array_form_of_integer` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0989_add_to_array_form_of_integer` |

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
.\scripts\test.ps1 -Folder 0989_add_to_array_form_of_integer -AllLanguages
```

```bash
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --all-languages
```

```zsh
./scripts/test.sh --folder 0989_add_to_array_form_of_integer --all-languages
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
