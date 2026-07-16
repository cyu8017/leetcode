# How We Solve Number of Digit One

Count ones digit by digit using higher, current, and lower parts of n.

## Steps

1. Process each decimal place with a growing factor.
2. Split n into higher, current digit, and lower segments.
3. Add the count contributed by that digit position.
4. Handle the special case when the current digit is 1.
5. Sum contributions across all digit positions.
