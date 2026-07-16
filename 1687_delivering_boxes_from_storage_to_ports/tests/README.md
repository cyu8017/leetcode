# Test harness for 1687_delivering_boxes_from_storage_to_ports

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language python
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language javascript
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language typescript
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language java
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language cpp
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language c
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language go
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language rust
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language kotlin
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language swift
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language ruby
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language csharp
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language scala
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language php
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm java java 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm c c 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm go go 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm rust rust 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm swift swift 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm scala scala 1687_delivering_boxes_from_storage_to_ports
docker compose -f docker/docker-compose.yml run --rm php php 1687_delivering_boxes_from_storage_to_ports
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1687_delivering_boxes_from_storage_to_ports` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1687_delivering_boxes_from_storage_to_ports` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1687_delivering_boxes_from_storage_to_ports` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1687_delivering_boxes_from_storage_to_ports` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1687_delivering_boxes_from_storage_to_ports` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1687_delivering_boxes_from_storage_to_ports` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1687_delivering_boxes_from_storage_to_ports` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1687_delivering_boxes_from_storage_to_ports` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1687_delivering_boxes_from_storage_to_ports` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1687_delivering_boxes_from_storage_to_ports` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1687_delivering_boxes_from_storage_to_ports` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1687_delivering_boxes_from_storage_to_ports` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1687_delivering_boxes_from_storage_to_ports` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1687_delivering_boxes_from_storage_to_ports` |

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
.\scripts\test.ps1 -Folder 1687_delivering_boxes_from_storage_to_ports -AllLanguages
```

```bash
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --all-languages
```

```zsh
./scripts/test.sh --folder 1687_delivering_boxes_from_storage_to_ports --all-languages
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
