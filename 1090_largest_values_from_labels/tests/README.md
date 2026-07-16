# Test harness for 1090_largest_values_from_labels

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1090_largest_values_from_labels --language python
./scripts/test.sh --folder 1090_largest_values_from_labels --language javascript
./scripts/test.sh --folder 1090_largest_values_from_labels --language typescript
./scripts/test.sh --folder 1090_largest_values_from_labels --language java
./scripts/test.sh --folder 1090_largest_values_from_labels --language cpp
./scripts/test.sh --folder 1090_largest_values_from_labels --language c
./scripts/test.sh --folder 1090_largest_values_from_labels --language go
./scripts/test.sh --folder 1090_largest_values_from_labels --language rust
./scripts/test.sh --folder 1090_largest_values_from_labels --language kotlin
./scripts/test.sh --folder 1090_largest_values_from_labels --language swift
./scripts/test.sh --folder 1090_largest_values_from_labels --language ruby
./scripts/test.sh --folder 1090_largest_values_from_labels --language csharp
./scripts/test.sh --folder 1090_largest_values_from_labels --language scala
./scripts/test.sh --folder 1090_largest_values_from_labels --language php
./scripts/test.sh --folder 1090_largest_values_from_labels --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1090_largest_values_from_labels --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm java java 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm c c 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm go go 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm rust rust 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm swift swift 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm scala scala 1090_largest_values_from_labels
docker compose -f docker/docker-compose.yml run --rm php php 1090_largest_values_from_labels
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1090_largest_values_from_labels` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1090_largest_values_from_labels` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1090_largest_values_from_labels` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1090_largest_values_from_labels` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1090_largest_values_from_labels` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1090_largest_values_from_labels` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1090_largest_values_from_labels` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1090_largest_values_from_labels` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1090_largest_values_from_labels` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1090_largest_values_from_labels` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1090_largest_values_from_labels` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1090_largest_values_from_labels` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1090_largest_values_from_labels` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1090_largest_values_from_labels` |

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
.\scripts\test.ps1 -Folder 1090_largest_values_from_labels -AllLanguages
```

```bash
./scripts/test.sh --folder 1090_largest_values_from_labels --all-languages
```

```zsh
./scripts/test.sh --folder 1090_largest_values_from_labels --all-languages
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
