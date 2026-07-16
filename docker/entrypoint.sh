#!/usr/bin/env bash
set -euo pipefail

LANGUAGE="${1:?language required}"
FOLDER="${2:?problem folder required}"
WORKSPACE="/workspace"
PROBLEM_DIR="${WORKSPACE}/${FOLDER}"

if [[ ! -d "${PROBLEM_DIR}" ]]; then
  echo "Problem folder not found: ${FOLDER}" >&2
  exit 1
fi

if [[ ! -f "${PROBLEM_DIR}/tests/cases.json" ]]; then
  echo "Missing tests folder for ${FOLDER}. Run scripts/scaffold-tests.ps1 first." >&2
  exit 1
fi

run_python() {
  python3 "${WORKSPACE}/runners/python/run_tests.py" "${PROBLEM_DIR}"
}

run_javascript() {
  node "${WORKSPACE}/runners/javascript/run_tests.mjs" "${PROBLEM_DIR}"
}

run_typescript() {
  node "${WORKSPACE}/runners/typescript/run_tests.mjs" "${PROBLEM_DIR}"
}

run_java() {
  python3 "${WORKSPACE}/runners/java/run_tests.py" "${PROBLEM_DIR}"
}

run_ruby() {
  ruby "${WORKSPACE}/runners/ruby/run_tests.rb" "${PROBLEM_DIR}"
}

run_php() {
  php "${WORKSPACE}/runners/php/run_tests.php" "${PROBLEM_DIR}"
}

run_cpp() {
  python3 "${WORKSPACE}/runners/cpp/run_tests.py" "${PROBLEM_DIR}"
}

run_compiled() {
  python3 "${WORKSPACE}/runners/compiled/run_compiled.py" "${LANGUAGE}" "${PROBLEM_DIR}"
}

case "${LANGUAGE}" in
  python) run_python ;;
  javascript) run_javascript ;;
  typescript) run_typescript ;;
  java) run_java ;;
  ruby) run_ruby ;;
  php) run_php ;;
  cpp) run_cpp ;;
  c|go|rust|kotlin|csharp|scala|swift) run_compiled ;;
  *)
    echo "Unknown language: ${LANGUAGE}" >&2
    exit 2
    ;;
esac
