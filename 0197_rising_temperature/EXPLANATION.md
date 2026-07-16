# How We Solve Rising Temperature

Compare each day's temperature with the previous calendar day.

## Steps

1. Self-join `Weather` so dates differ by one day.
2. Use `DATEDIFF` to enforce consecutive dates.
3. Keep rows warmer than the previous day.
4. Select those ids.
5. Return the rising-temperature days.
