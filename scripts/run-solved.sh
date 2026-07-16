#!/usr/bin/env bash
# Run tests for all problems in config/solved-problems.json
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

LOCAL=false
FAIL_FAST=false
FOLDER=""
LANGUAGES=()

usage() {
  cat <<EOF
Usage:
  ./scripts/run-solved.sh
  ./scripts/run-solved.sh --language python
  ./scripts/run-solved.sh --local
  ./scripts/run-solved.sh --folder 0001_two_sum
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --local) LOCAL=true; shift ;;
    --fail-fast) FAIL_FAST=true; shift ;;
    --folder|-f) FOLDER="$2"; shift 2 ;;
    --language|-l) LANGUAGES+=("$2"); shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

args=(python "${SCRIPT_DIR}/run-solved.py" --repo-root "${REPO_ROOT}")
if [[ "${LOCAL}" == true ]]; then args+=(--local); fi
if [[ "${FAIL_FAST}" == true ]]; then args+=(--fail-fast); fi
if [[ -n "${FOLDER}" ]]; then args+=(--folder "${FOLDER}"); fi
for lang in "${LANGUAGES[@]}"; do
  args+=(--language "${lang}")
done

exec "${args[@]}"
