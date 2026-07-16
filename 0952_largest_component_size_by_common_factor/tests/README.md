# Test harness for 0952_largest_component_size_by_common_factor

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language python
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language javascript
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language typescript
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language java
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language cpp
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language c
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language go
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language rust
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language kotlin
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language swift
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language ruby
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language csharp
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language scala
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language php
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm java java 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm c c 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm go go 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm rust rust 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm swift swift 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm scala scala 0952_largest_component_size_by_common_factor
docker compose -f docker/docker-compose.yml run --rm php php 0952_largest_component_size_by_common_factor
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0952_largest_component_size_by_common_factor` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0952_largest_component_size_by_common_factor` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0952_largest_component_size_by_common_factor` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0952_largest_component_size_by_common_factor` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0952_largest_component_size_by_common_factor` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0952_largest_component_size_by_common_factor` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0952_largest_component_size_by_common_factor` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0952_largest_component_size_by_common_factor` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0952_largest_component_size_by_common_factor` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0952_largest_component_size_by_common_factor` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0952_largest_component_size_by_common_factor` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0952_largest_component_size_by_common_factor` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0952_largest_component_size_by_common_factor` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0952_largest_component_size_by_common_factor` |

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
.\scripts\test.ps1 -Folder 0952_largest_component_size_by_common_factor -AllLanguages
```

```bash
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --all-languages
```

```zsh
./scripts/test.sh --folder 0952_largest_component_size_by_common_factor --all-languages
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
