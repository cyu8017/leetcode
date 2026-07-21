set -e
cd /workspace
fail=0
for f in '"$($folders -join ' ')"'; do
  echo "=== COMPILE $f ==="
  if ! swiftc -parse "$f/Solution.swift" 2>&1; then
    echo "FAIL: $f"
    fail=1
  else
    echo "OK: $f"
  fi
done
exit $fail
