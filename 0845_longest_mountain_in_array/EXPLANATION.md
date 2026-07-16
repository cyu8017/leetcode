# How We Solve Longest Mountain in Array

Scan for strictly ascending then descending segments.

## Steps

1. Walk while values increase, then while they decrease.
2. A valid mountain needs both an uphill and a downhill.
3. Track the maximum length of such windows.
