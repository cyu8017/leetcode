# Test harness for 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language python
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language javascript
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language typescript
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language java
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language cpp
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language c
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language go
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language rust
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language kotlin
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language swift
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language ruby
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language csharp
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language scala
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language php
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm java java 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm c c 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm go go 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm rust rust 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm swift swift 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm scala scala 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
docker compose -f docker/docker-compose.yml run --rm php php 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking` |

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
.\scripts\test.ps1 -Folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking -AllLanguages
```

```bash
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --all-languages
```

```zsh
./scripts/test.sh --folder 3391_design_a_3d_binary_matrix_with_efficient_layer_tracking --all-languages
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
