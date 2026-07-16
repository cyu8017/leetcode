# Test harness for 3259_maximum_energy_boost_from_two_drinks

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language python
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language javascript
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language typescript
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language java
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language cpp
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language c
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language go
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language rust
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language kotlin
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language swift
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language ruby
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language csharp
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language scala
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language php
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm java java 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm c c 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm go go 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm rust rust 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm swift swift 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm scala scala 3259_maximum_energy_boost_from_two_drinks
docker compose -f docker/docker-compose.yml run --rm php php 3259_maximum_energy_boost_from_two_drinks
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3259_maximum_energy_boost_from_two_drinks` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3259_maximum_energy_boost_from_two_drinks` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3259_maximum_energy_boost_from_two_drinks` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3259_maximum_energy_boost_from_two_drinks` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3259_maximum_energy_boost_from_two_drinks` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3259_maximum_energy_boost_from_two_drinks` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3259_maximum_energy_boost_from_two_drinks` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3259_maximum_energy_boost_from_two_drinks` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3259_maximum_energy_boost_from_two_drinks` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3259_maximum_energy_boost_from_two_drinks` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3259_maximum_energy_boost_from_two_drinks` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3259_maximum_energy_boost_from_two_drinks` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3259_maximum_energy_boost_from_two_drinks` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3259_maximum_energy_boost_from_two_drinks` |

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
.\scripts\test.ps1 -Folder 3259_maximum_energy_boost_from_two_drinks -AllLanguages
```

```bash
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --all-languages
```

```zsh
./scripts/test.sh --folder 3259_maximum_energy_boost_from_two_drinks --all-languages
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
