# Test harness for 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language python
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language javascript
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language typescript
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language java
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language cpp
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language c
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language go
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language rust
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language kotlin
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language swift
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language ruby
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language csharp
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language scala
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language php
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm java java 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm c c 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm go go 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm rust rust 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm swift swift 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm scala scala 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
docker compose -f docker/docker-compose.yml run --rm php php 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip` |

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
.\scripts\test.ps1 -Folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip -AllLanguages
```

```bash
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --all-languages
```

```zsh
./scripts/test.sh --folder 2556_disconnect_path_in_a_binary_matrix_by_at_most_one_flip --all-languages
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
