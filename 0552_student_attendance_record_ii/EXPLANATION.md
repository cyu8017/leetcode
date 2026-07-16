# How We Solve Student Attendance Record II

DP tracks absence count and trailing late streak while building valid length-`n` records.

## Steps

1. Let `dp[a][l]` be ways with `a` absences so far and `l` consecutive trailing lates.
2. From each state, append `P` (reset lates), `A` if `a == 0`, or `L` if `l < 2`.
3. Iterate `n` days modulo `10^9 + 7` and sum all ending states.
