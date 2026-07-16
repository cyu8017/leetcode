# How We Solve Investments in 2016

Sum 2016 investments for policies with a shared 2015 value and a unique city.

## Steps

1. Keep `tiv_2015` values that appear more than once.
2. Keep `(lat, lon)` pairs that appear exactly once.
3. Sum matching `tiv_2016` values and round to two decimals.
