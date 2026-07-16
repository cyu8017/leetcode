# Test harness for 0604_design_compressed_string_iterator

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language python
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language javascript
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language typescript
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language java
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language cpp
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language c
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language go
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language rust
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language kotlin
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language swift
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language ruby
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language csharp
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language scala
./scripts/test.sh --folder 0604_design_compressed_string_iterator --language php
./scripts/test.sh --folder 0604_design_compressed_string_iterator --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0604_design_compressed_string_iterator --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm java java 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm c c 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm go go 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm rust rust 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm swift swift 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm scala scala 0604_design_compressed_string_iterator
docker compose -f docker/docker-compose.yml run --rm php php 0604_design_compressed_string_iterator
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0604_design_compressed_string_iterator` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0604_design_compressed_string_iterator` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0604_design_compressed_string_iterator` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0604_design_compressed_string_iterator` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0604_design_compressed_string_iterator` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0604_design_compressed_string_iterator` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0604_design_compressed_string_iterator` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0604_design_compressed_string_iterator` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0604_design_compressed_string_iterator` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0604_design_compressed_string_iterator` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0604_design_compressed_string_iterator` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0604_design_compressed_string_iterator` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0604_design_compressed_string_iterator` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0604_design_compressed_string_iterator` |

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
.\scripts\test.ps1 -Folder 0604_design_compressed_string_iterator -AllLanguages
```

```bash
./scripts/test.sh --folder 0604_design_compressed_string_iterator --all-languages
```

```zsh
./scripts/test.sh --folder 0604_design_compressed_string_iterator --all-languages
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
