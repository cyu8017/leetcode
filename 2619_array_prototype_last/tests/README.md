# Test harness for 2619_array_prototype_last

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2619_array_prototype_last -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2619_array_prototype_last --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2619_array_prototype_last --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2619_array_prototype_last --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2619_array_prototype_last --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2619_array_prototype_last --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2619_array_prototype_last --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2619_array_prototype_last --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2619_array_prototype_last --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2619_array_prototype_last --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2619_array_prototype_last --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2619_array_prototype_last --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2619_array_prototype_last --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2619_array_prototype_last --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2619_array_prototype_last --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2619_array_prototype_last --language python
./scripts/test.sh --folder 2619_array_prototype_last --language javascript
./scripts/test.sh --folder 2619_array_prototype_last --language typescript
./scripts/test.sh --folder 2619_array_prototype_last --language java
./scripts/test.sh --folder 2619_array_prototype_last --language cpp
./scripts/test.sh --folder 2619_array_prototype_last --language c
./scripts/test.sh --folder 2619_array_prototype_last --language go
./scripts/test.sh --folder 2619_array_prototype_last --language rust
./scripts/test.sh --folder 2619_array_prototype_last --language kotlin
./scripts/test.sh --folder 2619_array_prototype_last --language swift
./scripts/test.sh --folder 2619_array_prototype_last --language ruby
./scripts/test.sh --folder 2619_array_prototype_last --language csharp
./scripts/test.sh --folder 2619_array_prototype_last --language scala
./scripts/test.sh --folder 2619_array_prototype_last --language php
./scripts/test.sh --folder 2619_array_prototype_last --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2619_array_prototype_last --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2619_array_prototype_last --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2619_array_prototype_last --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2619_array_prototype_last --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2619_array_prototype_last --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2619_array_prototype_last --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2619_array_prototype_last --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2619_array_prototype_last --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2619_array_prototype_last --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2619_array_prototype_last --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2619_array_prototype_last --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2619_array_prototype_last --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2619_array_prototype_last --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2619_array_prototype_last --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm java java 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm c c 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm go go 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm rust rust 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm swift swift 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm scala scala 2619_array_prototype_last
docker compose -f docker/docker-compose.yml run --rm php php 2619_array_prototype_last
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2619_array_prototype_last` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2619_array_prototype_last` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2619_array_prototype_last` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2619_array_prototype_last` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2619_array_prototype_last` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2619_array_prototype_last` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2619_array_prototype_last` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2619_array_prototype_last` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2619_array_prototype_last` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2619_array_prototype_last` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2619_array_prototype_last` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2619_array_prototype_last` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2619_array_prototype_last` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2619_array_prototype_last` |

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
.\scripts\test.ps1 -Folder 2619_array_prototype_last -AllLanguages
```

```bash
./scripts/test.sh --folder 2619_array_prototype_last --all-languages
```

```zsh
./scripts/test.sh --folder 2619_array_prototype_last --all-languages
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
