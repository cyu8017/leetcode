# How We Solve Ugly Number II

Generate ugly numbers in order using three moving pointers.

## Steps

1. Start the sequence with 1.
2. Track the next candidate from multiples of 2, 3, and 5.
3. Append the smallest candidate.
4. Advance every pointer that produced that candidate.
5. Return the nth generated ugly number.
