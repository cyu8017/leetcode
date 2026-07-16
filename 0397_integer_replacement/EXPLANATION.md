# How We Solve Integer Replacement

Greedy parity rules minimize the path from n down to 1.

## Steps

1. Halve even numbers.
2. For odd n, prefer n-1 when n % 4 == 1 or n == 3; otherwise n+1.
3. Count each operation until reaching 1.
