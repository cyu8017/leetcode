# Test harness for 1325_delete_leaves_with_a_given_value

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language python
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language javascript
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language typescript
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language java
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language cpp
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language c
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language go
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language rust
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language kotlin
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language swift
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language ruby
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language csharp
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language scala
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language php
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm java java 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm c c 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm go go 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm rust rust 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm swift swift 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm scala scala 1325_delete_leaves_with_a_given_value
docker compose -f docker/docker-compose.yml run --rm php php 1325_delete_leaves_with_a_given_value
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1325_delete_leaves_with_a_given_value` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1325_delete_leaves_with_a_given_value` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1325_delete_leaves_with_a_given_value` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1325_delete_leaves_with_a_given_value` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1325_delete_leaves_with_a_given_value` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1325_delete_leaves_with_a_given_value` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1325_delete_leaves_with_a_given_value` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1325_delete_leaves_with_a_given_value` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1325_delete_leaves_with_a_given_value` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1325_delete_leaves_with_a_given_value` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1325_delete_leaves_with_a_given_value` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1325_delete_leaves_with_a_given_value` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1325_delete_leaves_with_a_given_value` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1325_delete_leaves_with_a_given_value` |

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
.\scripts\test.ps1 -Folder 1325_delete_leaves_with_a_given_value -AllLanguages
```

```bash
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --all-languages
```

```zsh
./scripts/test.sh --folder 1325_delete_leaves_with_a_given_value --all-languages
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
