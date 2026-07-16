# Test harness for 2823_deep_object_filter

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2823_deep_object_filter -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2823_deep_object_filter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2823_deep_object_filter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2823_deep_object_filter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2823_deep_object_filter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2823_deep_object_filter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2823_deep_object_filter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2823_deep_object_filter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2823_deep_object_filter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2823_deep_object_filter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2823_deep_object_filter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2823_deep_object_filter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2823_deep_object_filter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2823_deep_object_filter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2823_deep_object_filter --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2823_deep_object_filter --language python
./scripts/test.sh --folder 2823_deep_object_filter --language javascript
./scripts/test.sh --folder 2823_deep_object_filter --language typescript
./scripts/test.sh --folder 2823_deep_object_filter --language java
./scripts/test.sh --folder 2823_deep_object_filter --language cpp
./scripts/test.sh --folder 2823_deep_object_filter --language c
./scripts/test.sh --folder 2823_deep_object_filter --language go
./scripts/test.sh --folder 2823_deep_object_filter --language rust
./scripts/test.sh --folder 2823_deep_object_filter --language kotlin
./scripts/test.sh --folder 2823_deep_object_filter --language swift
./scripts/test.sh --folder 2823_deep_object_filter --language ruby
./scripts/test.sh --folder 2823_deep_object_filter --language csharp
./scripts/test.sh --folder 2823_deep_object_filter --language scala
./scripts/test.sh --folder 2823_deep_object_filter --language php
./scripts/test.sh --folder 2823_deep_object_filter --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2823_deep_object_filter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2823_deep_object_filter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2823_deep_object_filter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2823_deep_object_filter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2823_deep_object_filter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2823_deep_object_filter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2823_deep_object_filter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2823_deep_object_filter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2823_deep_object_filter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2823_deep_object_filter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2823_deep_object_filter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2823_deep_object_filter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2823_deep_object_filter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2823_deep_object_filter --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm java java 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm c c 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm go go 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm rust rust 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm swift swift 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm scala scala 2823_deep_object_filter
docker compose -f docker/docker-compose.yml run --rm php php 2823_deep_object_filter
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2823_deep_object_filter` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2823_deep_object_filter` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2823_deep_object_filter` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2823_deep_object_filter` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2823_deep_object_filter` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2823_deep_object_filter` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2823_deep_object_filter` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2823_deep_object_filter` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2823_deep_object_filter` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2823_deep_object_filter` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2823_deep_object_filter` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2823_deep_object_filter` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2823_deep_object_filter` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2823_deep_object_filter` |

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
.\scripts\test.ps1 -Folder 2823_deep_object_filter -AllLanguages
```

```bash
./scripts/test.sh --folder 2823_deep_object_filter --all-languages
```

```zsh
./scripts/test.sh --folder 2823_deep_object_filter --all-languages
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
