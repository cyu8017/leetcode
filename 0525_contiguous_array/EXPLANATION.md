# How We Solve Contiguous Array

Map zeros to -1 and ones to +1, then seek the longest zero-sum subarray.

## Steps

1. Track running balance while scanning the array.
2. Store the first index where each balance occurs.
3. Maximize distance between equal balances.
