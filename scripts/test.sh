#!/usr/bin/env bash
# Cross-platform test runner — requires Docker only.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMPOSE_FILE="${REPO_ROOT}/docker/docker-compose.yml"

FOLDER=""
LANGUAGE=""
ALL_LANGUAGES=false

usage() {
  cat <<EOF
Usage:
  ./scripts/test.sh --folder 0001_two_sum --language python
  ./scripts/test.sh --folder 0001_two_sum --all-languages

Requires Docker. Toolchain versions are pinned in docker/docker-compose.yml.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --folder|-f) FOLDER="$2"; shift 2 ;;
    --language|-l) LANGUAGE="$2"; shift 2 ;;
    --all-languages|-a) ALL_LANGUAGES=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

if [[ -z "${FOLDER}" ]]; then
  echo "Missing --folder" >&2
  usage
  exit 2
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is required. Install Docker Desktop and try again." >&2
  exit 1
fi

run_language() {
  local lang="$1"
  echo ""
  echo "==> Testing ${lang} (Docker)"
  docker compose -f "${COMPOSE_FILE}" run --rm "${lang}" "${lang}" "${FOLDER}"
}

if [[ "${ALL_LANGUAGES}" == true ]]; then
  languages=(python javascript typescript java ruby php cpp c go rust csharp kotlin scala swift)
  failures=0
  for lang in "${languages[@]}"; do
    if ! run_language "${lang}"; then
      failures=$((failures + 1))
    fi
  done
  echo ""
  echo "All-language summary: ${failures} language runner(s) failed"
  exit "${failures}"
fi

if [[ -z "${LANGUAGE}" ]]; then
  echo "Specify --language or --all-languages" >&2
  usage
  exit 2
fi

run_language "${LANGUAGE}"
