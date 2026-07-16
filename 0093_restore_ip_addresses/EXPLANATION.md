# How We Solve Restore IP Addresses

Split a digit string into all valid IP addresses.

## Steps

1. Build an IP with exactly four parts.
2. Each part is 1–3 digits and its value is at most 255.
3. Skip parts with leading zeros unless the part is just 0.
4. Backtrack through all valid splits.
5. Join successful parts with dots.
