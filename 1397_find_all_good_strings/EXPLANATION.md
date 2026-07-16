# 1397. Find All Good Strings

## Approach
Digit DP enforces both lexical bounds while KMP state rejects strings containing evil.

## Complexity
O(n·|evil|·26) time and O(n·|evil|) space.
