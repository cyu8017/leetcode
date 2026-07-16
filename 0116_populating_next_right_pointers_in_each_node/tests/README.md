# Test harness for 0116_populating_next_right_pointers_in_each_node

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language python
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language javascript
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language typescript
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language java
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language cpp
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language c
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language go
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language rust
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language kotlin
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language swift
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language ruby
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language csharp
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language scala
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language php
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm java java 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm c c 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm go go 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm rust rust 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm swift swift 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm scala scala 0116_populating_next_right_pointers_in_each_node
docker compose -f docker/docker-compose.yml run --rm php php 0116_populating_next_right_pointers_in_each_node
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0116_populating_next_right_pointers_in_each_node` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0116_populating_next_right_pointers_in_each_node` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0116_populating_next_right_pointers_in_each_node` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0116_populating_next_right_pointers_in_each_node` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0116_populating_next_right_pointers_in_each_node` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0116_populating_next_right_pointers_in_each_node` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0116_populating_next_right_pointers_in_each_node` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0116_populating_next_right_pointers_in_each_node` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0116_populating_next_right_pointers_in_each_node` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0116_populating_next_right_pointers_in_each_node` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0116_populating_next_right_pointers_in_each_node` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0116_populating_next_right_pointers_in_each_node` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0116_populating_next_right_pointers_in_each_node` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0116_populating_next_right_pointers_in_each_node` |

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
.\scripts\test.ps1 -Folder 0116_populating_next_right_pointers_in_each_node -AllLanguages
```

```bash
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --all-languages
```

```zsh
./scripts/test.sh --folder 0116_populating_next_right_pointers_in_each_node --all-languages
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
