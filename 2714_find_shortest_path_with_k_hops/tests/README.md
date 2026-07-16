# Test harness for 2714_find_shortest_path_with_k_hops

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language python
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language javascript
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language typescript
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language java
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language cpp
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language c
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language go
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language rust
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language kotlin
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language swift
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language ruby
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language csharp
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language scala
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language php
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm java java 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm c c 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm go go 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm rust rust 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm swift swift 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm scala scala 2714_find_shortest_path_with_k_hops
docker compose -f docker/docker-compose.yml run --rm php php 2714_find_shortest_path_with_k_hops
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2714_find_shortest_path_with_k_hops` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2714_find_shortest_path_with_k_hops` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2714_find_shortest_path_with_k_hops` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2714_find_shortest_path_with_k_hops` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2714_find_shortest_path_with_k_hops` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2714_find_shortest_path_with_k_hops` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2714_find_shortest_path_with_k_hops` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2714_find_shortest_path_with_k_hops` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2714_find_shortest_path_with_k_hops` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2714_find_shortest_path_with_k_hops` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2714_find_shortest_path_with_k_hops` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2714_find_shortest_path_with_k_hops` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2714_find_shortest_path_with_k_hops` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2714_find_shortest_path_with_k_hops` |

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
.\scripts\test.ps1 -Folder 2714_find_shortest_path_with_k_hops -AllLanguages
```

```bash
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --all-languages
```

```zsh
./scripts/test.sh --folder 2714_find_shortest_path_with_k_hops --all-languages
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
