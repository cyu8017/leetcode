#!/usr/bin/env bash
set -u
SKIP="1050 1068 1069 1070 1075 1076 1077 1082 1083 1084 1097 1098"
PASS=0
FAIL=0
STUB=0
FAILS=""
cd /workspace
for dir in 10[5-9][0-9]_*/; do
  name=$(basename "$dir")
  num=${name:0:4}
  if echo " $SKIP " | grep -q " $num "; then
    continue
  fi
  rs="${dir}solution.rs"
  if grep -q "pub fn solve()" "$rs"; then
    STUB=$((STUB+1))
    FAILS="${FAILS}
STUB ${name}"
    continue
  fi
  tmp=$(mktemp /tmp/rsXXXXXX.rs)
  printf 'struct Solution;\n' > "$tmp"
  cat "$rs" >> "$tmp"
  out=$(mktemp /tmp/rlibXXXXXX.rlib)
  if rustc --edition 2021 --crate-type lib "$tmp" -o "$out" 2>/tmp/rustcerr; then
    PASS=$((PASS+1))
  else
    FAIL=$((FAIL+1))
    FAILS="${FAILS}
FAIL ${name}:
$(cat /tmp/rustcerr)"
  fi
  rm -f "$tmp" "$out"
done
echo "PASS=$PASS FAIL=$FAIL STUB=$STUB"
echo "$FAILS"
