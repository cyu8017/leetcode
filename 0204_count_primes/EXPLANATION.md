# How We Solve Count Primes

Use the Sieve of Eratosthenes to mark composites below `n`.

## Steps

1. Return 0 when `n` is at most 2.
2. Create a boolean array marking every index as potentially prime.
3. For each prime `p`, mark multiples starting at `p*p`.
4. Continue while `p*p < n`.
5. Count the remaining true entries.
