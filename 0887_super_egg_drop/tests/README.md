# Test harness for 0887_super_egg_drop

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0887_super_egg_drop -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0887_super_egg_drop --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0887_super_egg_drop --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0887_super_egg_drop --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0887_super_egg_drop --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0887_super_egg_drop --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0887_super_egg_drop --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0887_super_egg_drop --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0887_super_egg_drop --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0887_super_egg_drop --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0887_super_egg_drop --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0887_super_egg_drop --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0887_super_egg_drop --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0887_super_egg_drop --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0887_super_egg_drop --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0887_super_egg_drop --language python
./scripts/test.sh --folder 0887_super_egg_drop --language javascript
./scripts/test.sh --folder 0887_super_egg_drop --language typescript
./scripts/test.sh --folder 0887_super_egg_drop --language java
./scripts/test.sh --folder 0887_super_egg_drop --language cpp
./scripts/test.sh --folder 0887_super_egg_drop --language c
./scripts/test.sh --folder 0887_super_egg_drop --language go
./scripts/test.sh --folder 0887_super_egg_drop --language rust
./scripts/test.sh --folder 0887_super_egg_drop --language kotlin
./scripts/test.sh --folder 0887_super_egg_drop --language swift
./scripts/test.sh --folder 0887_super_egg_drop --language ruby
./scripts/test.sh --folder 0887_super_egg_drop --language csharp
./scripts/test.sh --folder 0887_super_egg_drop --language scala
./scripts/test.sh --folder 0887_super_egg_drop --language php
./scripts/test.sh --folder 0887_super_egg_drop --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0887_super_egg_drop --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0887_super_egg_drop --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0887_super_egg_drop --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0887_super_egg_drop --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0887_super_egg_drop --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0887_super_egg_drop --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0887_super_egg_drop --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0887_super_egg_drop --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0887_super_egg_drop --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0887_super_egg_drop --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0887_super_egg_drop --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0887_super_egg_drop --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0887_super_egg_drop --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0887_super_egg_drop --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm java java 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm c c 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm go go 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm rust rust 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm swift swift 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm scala scala 0887_super_egg_drop
docker compose -f docker/docker-compose.yml run --rm php php 0887_super_egg_drop
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0887_super_egg_drop` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0887_super_egg_drop` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0887_super_egg_drop` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0887_super_egg_drop` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0887_super_egg_drop` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0887_super_egg_drop` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0887_super_egg_drop` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0887_super_egg_drop` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0887_super_egg_drop` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0887_super_egg_drop` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0887_super_egg_drop` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0887_super_egg_drop` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0887_super_egg_drop` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0887_super_egg_drop` |

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
.\scripts\test.ps1 -Folder 0887_super_egg_drop -AllLanguages
```

```bash
./scripts/test.sh --folder 0887_super_egg_drop --all-languages
```

```zsh
./scripts/test.sh --folder 0887_super_egg_drop --all-languages
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
