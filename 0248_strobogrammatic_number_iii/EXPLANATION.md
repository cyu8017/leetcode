# How We Solve Strobogrammatic Number III

Generate strobogrammatic numbers by length and count those in the numeric range.

## Steps

1. Loop over every length between `low` and `high`.
2. Generate all strobogrammatic strings of that length.
3. Convert bounds and candidates to integers for comparison.
4. Count values inside the inclusive range.
5. Return the total count.
