# Test harness for 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language python
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language javascript
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language typescript
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language java
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language cpp
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language c
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language go
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language rust
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language kotlin
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language swift
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language ruby
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language csharp
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language scala
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language php
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm java java 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm c c 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm go go 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm rust rust 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm swift swift 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm scala scala 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
docker compose -f docker/docker-compose.yml run --rm php php 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period` |

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
.\scripts\test.ps1 -Folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period -AllLanguages
```

```bash
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --all-languages
```

```zsh
./scripts/test.sh --folder 1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period --all-languages
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
