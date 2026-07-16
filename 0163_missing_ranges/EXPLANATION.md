# How We Solve Missing Ranges

Scan the sorted numbers and emit every gap inside `[lower, upper]`.

## Steps

1. Start with a sentinel just before `lower`.
2. Walk each number plus a sentinel just after `upper`.
3. Whenever the gap is at least two, record `[prev+1, num-1]`.
4. Update `prev` to the current number.
5. Return the collected inclusive ranges.
