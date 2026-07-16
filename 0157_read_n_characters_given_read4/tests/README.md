# Test harness for 0157_read_n_characters_given_read4

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language python
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language javascript
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language typescript
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language java
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language cpp
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language c
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language go
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language rust
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language kotlin
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language swift
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language ruby
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language csharp
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language scala
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language php
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0157_read_n_characters_given_read4 --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm java java 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm c c 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm go go 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm rust rust 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm swift swift 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm scala scala 0157_read_n_characters_given_read4
docker compose -f docker/docker-compose.yml run --rm php php 0157_read_n_characters_given_read4
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0157_read_n_characters_given_read4` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0157_read_n_characters_given_read4` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0157_read_n_characters_given_read4` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0157_read_n_characters_given_read4` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0157_read_n_characters_given_read4` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0157_read_n_characters_given_read4` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0157_read_n_characters_given_read4` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0157_read_n_characters_given_read4` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0157_read_n_characters_given_read4` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0157_read_n_characters_given_read4` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0157_read_n_characters_given_read4` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0157_read_n_characters_given_read4` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0157_read_n_characters_given_read4` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0157_read_n_characters_given_read4` |

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
.\scripts\test.ps1 -Folder 0157_read_n_characters_given_read4 -AllLanguages
```

```bash
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --all-languages
```

```zsh
./scripts/test.sh --folder 0157_read_n_characters_given_read4 --all-languages
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
