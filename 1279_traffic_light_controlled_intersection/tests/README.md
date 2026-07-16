# Test harness for 1279_traffic_light_controlled_intersection

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language python
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language javascript
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language typescript
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language java
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language cpp
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language c
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language go
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language rust
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language kotlin
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language swift
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language ruby
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language csharp
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language scala
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language php
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm java java 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm c c 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm go go 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm rust rust 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm swift swift 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm scala scala 1279_traffic_light_controlled_intersection
docker compose -f docker/docker-compose.yml run --rm php php 1279_traffic_light_controlled_intersection
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1279_traffic_light_controlled_intersection` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1279_traffic_light_controlled_intersection` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1279_traffic_light_controlled_intersection` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1279_traffic_light_controlled_intersection` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1279_traffic_light_controlled_intersection` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1279_traffic_light_controlled_intersection` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1279_traffic_light_controlled_intersection` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1279_traffic_light_controlled_intersection` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1279_traffic_light_controlled_intersection` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1279_traffic_light_controlled_intersection` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1279_traffic_light_controlled_intersection` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1279_traffic_light_controlled_intersection` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1279_traffic_light_controlled_intersection` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1279_traffic_light_controlled_intersection` |

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
.\scripts\test.ps1 -Folder 1279_traffic_light_controlled_intersection -AllLanguages
```

```bash
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --all-languages
```

```zsh
./scripts/test.sh --folder 1279_traffic_light_controlled_intersection --all-languages
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
