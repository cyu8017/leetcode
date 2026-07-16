# Test harness for 1224_maximum_equal_frequency

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1224_maximum_equal_frequency --language python
./scripts/test.sh --folder 1224_maximum_equal_frequency --language javascript
./scripts/test.sh --folder 1224_maximum_equal_frequency --language typescript
./scripts/test.sh --folder 1224_maximum_equal_frequency --language java
./scripts/test.sh --folder 1224_maximum_equal_frequency --language cpp
./scripts/test.sh --folder 1224_maximum_equal_frequency --language c
./scripts/test.sh --folder 1224_maximum_equal_frequency --language go
./scripts/test.sh --folder 1224_maximum_equal_frequency --language rust
./scripts/test.sh --folder 1224_maximum_equal_frequency --language kotlin
./scripts/test.sh --folder 1224_maximum_equal_frequency --language swift
./scripts/test.sh --folder 1224_maximum_equal_frequency --language ruby
./scripts/test.sh --folder 1224_maximum_equal_frequency --language csharp
./scripts/test.sh --folder 1224_maximum_equal_frequency --language scala
./scripts/test.sh --folder 1224_maximum_equal_frequency --language php
./scripts/test.sh --folder 1224_maximum_equal_frequency --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1224_maximum_equal_frequency --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm java java 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm c c 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm go go 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm rust rust 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm swift swift 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm scala scala 1224_maximum_equal_frequency
docker compose -f docker/docker-compose.yml run --rm php php 1224_maximum_equal_frequency
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1224_maximum_equal_frequency` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1224_maximum_equal_frequency` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1224_maximum_equal_frequency` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1224_maximum_equal_frequency` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1224_maximum_equal_frequency` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1224_maximum_equal_frequency` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1224_maximum_equal_frequency` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1224_maximum_equal_frequency` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1224_maximum_equal_frequency` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1224_maximum_equal_frequency` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1224_maximum_equal_frequency` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1224_maximum_equal_frequency` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1224_maximum_equal_frequency` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1224_maximum_equal_frequency` |

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
.\scripts\test.ps1 -Folder 1224_maximum_equal_frequency -AllLanguages
```

```bash
./scripts/test.sh --folder 1224_maximum_equal_frequency --all-languages
```

```zsh
./scripts/test.sh --folder 1224_maximum_equal_frequency --all-languages
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
