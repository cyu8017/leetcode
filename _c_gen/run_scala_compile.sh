#!/bin/bash
set -euo pipefail
export PATH="/usr/local/bin:/opt/scala-2.13.14/bin:$PATH"
OUT=/workspace/_c_gen/scala_compile_result.txt
{
  echo "scalac=$(command -v scalac)"
  scalac -version 2>&1 || true
  bash /workspace/_c_gen/compile_check_scala_1801_1850.sh
} >"$OUT" 2>&1
echo "wrote $OUT"
