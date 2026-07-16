# Test harness for 3890_integers_with_multiple_sum_of_two_cubes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language python
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language javascript
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language typescript
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language java
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language cpp
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language c
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language go
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language rust
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language kotlin
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language swift
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language ruby
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language csharp
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language scala
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language php
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm java java 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm c c 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm go go 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm rust rust 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm swift swift 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm scala scala 3890_integers_with_multiple_sum_of_two_cubes
docker compose -f docker/docker-compose.yml run --rm php php 3890_integers_with_multiple_sum_of_two_cubes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3890_integers_with_multiple_sum_of_two_cubes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3890_integers_with_multiple_sum_of_two_cubes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3890_integers_with_multiple_sum_of_two_cubes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3890_integers_with_multiple_sum_of_two_cubes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3890_integers_with_multiple_sum_of_two_cubes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3890_integers_with_multiple_sum_of_two_cubes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3890_integers_with_multiple_sum_of_two_cubes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3890_integers_with_multiple_sum_of_two_cubes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3890_integers_with_multiple_sum_of_two_cubes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3890_integers_with_multiple_sum_of_two_cubes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3890_integers_with_multiple_sum_of_two_cubes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3890_integers_with_multiple_sum_of_two_cubes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3890_integers_with_multiple_sum_of_two_cubes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3890_integers_with_multiple_sum_of_two_cubes` |

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
.\scripts\test.ps1 -Folder 3890_integers_with_multiple_sum_of_two_cubes -AllLanguages
```

```bash
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --all-languages
```

```zsh
./scripts/test.sh --folder 3890_integers_with_multiple_sum_of_two_cubes --all-languages
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
