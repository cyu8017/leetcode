# Test harness for 3186_maximum_total_damage_with_spell_casting

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language python
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language javascript
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language typescript
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language java
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language cpp
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language c
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language go
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language rust
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language kotlin
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language swift
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language ruby
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language csharp
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language scala
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language php
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm java java 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm c c 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm go go 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm rust rust 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm swift swift 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm scala scala 3186_maximum_total_damage_with_spell_casting
docker compose -f docker/docker-compose.yml run --rm php php 3186_maximum_total_damage_with_spell_casting
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3186_maximum_total_damage_with_spell_casting` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3186_maximum_total_damage_with_spell_casting` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3186_maximum_total_damage_with_spell_casting` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3186_maximum_total_damage_with_spell_casting` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3186_maximum_total_damage_with_spell_casting` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3186_maximum_total_damage_with_spell_casting` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3186_maximum_total_damage_with_spell_casting` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3186_maximum_total_damage_with_spell_casting` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3186_maximum_total_damage_with_spell_casting` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3186_maximum_total_damage_with_spell_casting` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3186_maximum_total_damage_with_spell_casting` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3186_maximum_total_damage_with_spell_casting` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3186_maximum_total_damage_with_spell_casting` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3186_maximum_total_damage_with_spell_casting` |

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
.\scripts\test.ps1 -Folder 3186_maximum_total_damage_with_spell_casting -AllLanguages
```

```bash
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --all-languages
```

```zsh
./scripts/test.sh --folder 3186_maximum_total_damage_with_spell_casting --all-languages
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
