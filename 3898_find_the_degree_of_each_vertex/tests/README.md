# Test harness for 3898_find_the_degree_of_each_vertex

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language python
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language javascript
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language typescript
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language java
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language cpp
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language c
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language go
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language rust
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language kotlin
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language swift
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language ruby
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language csharp
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language scala
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language php
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm java java 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm c c 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm go go 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm rust rust 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm swift swift 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm scala scala 3898_find_the_degree_of_each_vertex
docker compose -f docker/docker-compose.yml run --rm php php 3898_find_the_degree_of_each_vertex
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3898_find_the_degree_of_each_vertex` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3898_find_the_degree_of_each_vertex` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3898_find_the_degree_of_each_vertex` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3898_find_the_degree_of_each_vertex` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3898_find_the_degree_of_each_vertex` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3898_find_the_degree_of_each_vertex` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3898_find_the_degree_of_each_vertex` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3898_find_the_degree_of_each_vertex` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3898_find_the_degree_of_each_vertex` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3898_find_the_degree_of_each_vertex` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3898_find_the_degree_of_each_vertex` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3898_find_the_degree_of_each_vertex` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3898_find_the_degree_of_each_vertex` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3898_find_the_degree_of_each_vertex` |

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
.\scripts\test.ps1 -Folder 3898_find_the_degree_of_each_vertex -AllLanguages
```

```bash
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --all-languages
```

```zsh
./scripts/test.sh --folder 3898_find_the_degree_of_each_vertex --all-languages
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
