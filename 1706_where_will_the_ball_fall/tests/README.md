# Test harness for 1706_where_will_the_ball_fall

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language python
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language javascript
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language typescript
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language java
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language cpp
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language c
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language go
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language rust
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language kotlin
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language swift
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language ruby
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language csharp
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language scala
./scripts/test.sh --folder 1706_where_will_the_ball_fall --language php
./scripts/test.sh --folder 1706_where_will_the_ball_fall --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1706_where_will_the_ball_fall --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm java java 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm c c 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm go go 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm rust rust 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm swift swift 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm scala scala 1706_where_will_the_ball_fall
docker compose -f docker/docker-compose.yml run --rm php php 1706_where_will_the_ball_fall
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1706_where_will_the_ball_fall` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1706_where_will_the_ball_fall` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1706_where_will_the_ball_fall` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1706_where_will_the_ball_fall` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1706_where_will_the_ball_fall` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1706_where_will_the_ball_fall` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1706_where_will_the_ball_fall` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1706_where_will_the_ball_fall` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1706_where_will_the_ball_fall` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1706_where_will_the_ball_fall` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1706_where_will_the_ball_fall` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1706_where_will_the_ball_fall` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1706_where_will_the_ball_fall` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1706_where_will_the_ball_fall` |

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
.\scripts\test.ps1 -Folder 1706_where_will_the_ball_fall -AllLanguages
```

```bash
./scripts/test.sh --folder 1706_where_will_the_ball_fall --all-languages
```

```zsh
./scripts/test.sh --folder 1706_where_will_the_ball_fall --all-languages
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
