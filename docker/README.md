# Docker-based testing — pinned toolchains, no local installs required.

Pin file versions in `docker-compose.yml` when upgrading.

Pre-build all images once:

```bash
docker compose -f docker/docker-compose.yml build
```

Run a test:

```bash
# Windows
.\scripts\test.ps1 -Folder 0001_two_sum -Language python

# macOS / Linux
./scripts/test.sh --folder 0001_two_sum --language python
```

## Pinned versions

| Service | Image / base |
|---------|----------------|
| python | python:3.12.4-bookworm |
| javascript / typescript | node:20.14.0-bookworm + TypeScript 5.4.5 |
| java / kotlin / scala | eclipse-temurin:21.0.4_7-jdk-jammy + Python 3 |
| ruby | ruby:3.3.4-bookworm |
| php | php:8.3.9-cli-bookworm |
| cpp / c | gcc:14.1.0-bookworm + Python 3 |
| go | golang:1.22.5-bookworm + Python 3 |
| rust | rust:1.79.0-bookworm + Python 3 |
| csharp | dotnet/sdk:8.0.303-bookworm-slim + Python 3 |
| swift | swift:5.10.1-jammy |

When implementing a solution:

1. Update `tests/config.json` with the correct LeetCode method name
2. Add cases to `tests/cases.json`
3. Run `.\scripts\test.ps1 -Folder <problem> -Language <lang>` (Docker)

Every contributor gets the same versions regardless of host OS.
