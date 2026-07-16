# How We Solve Bulls and Cows

Count exact matches separately from digit frequency overlaps.

## Steps

1. Count bulls where secret and guess digits match at the same index.
2. Track unmatched digit frequencies in both strings.
3. Sum min counts per digit for cows.
4. Format the result as bulls A cows B.
