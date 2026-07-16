# How We Solve Consecutive Numbers Sum

`n` as `k` consecutive positives means `(n - k(k-1)/2)` is divisible by `k`.

## Steps

1. Enumerate length `k` while `k(k-1)/2 < n`.
2. Check if the remaining sum forms a valid starting integer.
3. Count valid `k` (including the trivial `k = 1`).
