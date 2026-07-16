# How We Solve Teemo Attacking

Sum poison durations, capping overlap between consecutive attacks.

## Steps

1. Start with one full duration for the first attack.
2. For each later attack, add min(duration, gap since previous).
3. Return the total poisoned time.
