# Test harness for 0612_shortest_distance_in_a_plane

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language python
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language javascript
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language typescript
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language java
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language cpp
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language c
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language go
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language rust
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language kotlin
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language swift
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language ruby
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language csharp
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language scala
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language php
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm java java 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm c c 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm go go 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm rust rust 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm swift swift 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm scala scala 0612_shortest_distance_in_a_plane
docker compose -f docker/docker-compose.yml run --rm php php 0612_shortest_distance_in_a_plane
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0612_shortest_distance_in_a_plane` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0612_shortest_distance_in_a_plane` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0612_shortest_distance_in_a_plane` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0612_shortest_distance_in_a_plane` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0612_shortest_distance_in_a_plane` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0612_shortest_distance_in_a_plane` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0612_shortest_distance_in_a_plane` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0612_shortest_distance_in_a_plane` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0612_shortest_distance_in_a_plane` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0612_shortest_distance_in_a_plane` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0612_shortest_distance_in_a_plane` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0612_shortest_distance_in_a_plane` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0612_shortest_distance_in_a_plane` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0612_shortest_distance_in_a_plane` |

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
.\scripts\test.ps1 -Folder 0612_shortest_distance_in_a_plane -AllLanguages
```

```bash
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --all-languages
```

```zsh
./scripts/test.sh --folder 0612_shortest_distance_in_a_plane --all-languages
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
