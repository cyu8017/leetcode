# Test harness for 1785_minimum_elements_to_add_to_form_a_given_sum

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language python
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language javascript
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language typescript
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language java
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language cpp
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language c
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language go
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language rust
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language kotlin
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language swift
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language ruby
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language csharp
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language scala
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language php
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm java java 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm c c 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm go go 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm rust rust 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm swift swift 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm scala scala 1785_minimum_elements_to_add_to_form_a_given_sum
docker compose -f docker/docker-compose.yml run --rm php php 1785_minimum_elements_to_add_to_form_a_given_sum
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1785_minimum_elements_to_add_to_form_a_given_sum` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1785_minimum_elements_to_add_to_form_a_given_sum` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1785_minimum_elements_to_add_to_form_a_given_sum` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1785_minimum_elements_to_add_to_form_a_given_sum` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1785_minimum_elements_to_add_to_form_a_given_sum` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1785_minimum_elements_to_add_to_form_a_given_sum` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1785_minimum_elements_to_add_to_form_a_given_sum` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1785_minimum_elements_to_add_to_form_a_given_sum` |

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
.\scripts\test.ps1 -Folder 1785_minimum_elements_to_add_to_form_a_given_sum -AllLanguages
```

```bash
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --all-languages
```

```zsh
./scripts/test.sh --folder 1785_minimum_elements_to_add_to_form_a_given_sum --all-languages
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
