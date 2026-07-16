# Test harness for 0984_string_without_aaa_or_bbb

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language python
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language javascript
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language typescript
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language java
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language cpp
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language c
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language go
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language rust
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language kotlin
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language swift
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language ruby
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language csharp
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language scala
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language php
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm java java 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm c c 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm go go 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm rust rust 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm swift swift 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm scala scala 0984_string_without_aaa_or_bbb
docker compose -f docker/docker-compose.yml run --rm php php 0984_string_without_aaa_or_bbb
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0984_string_without_aaa_or_bbb` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0984_string_without_aaa_or_bbb` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0984_string_without_aaa_or_bbb` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0984_string_without_aaa_or_bbb` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0984_string_without_aaa_or_bbb` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0984_string_without_aaa_or_bbb` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0984_string_without_aaa_or_bbb` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0984_string_without_aaa_or_bbb` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0984_string_without_aaa_or_bbb` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0984_string_without_aaa_or_bbb` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0984_string_without_aaa_or_bbb` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0984_string_without_aaa_or_bbb` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0984_string_without_aaa_or_bbb` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0984_string_without_aaa_or_bbb` |

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
.\scripts\test.ps1 -Folder 0984_string_without_aaa_or_bbb -AllLanguages
```

```bash
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --all-languages
```

```zsh
./scripts/test.sh --folder 0984_string_without_aaa_or_bbb --all-languages
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
