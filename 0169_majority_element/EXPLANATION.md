# How We Solve Majority Element

Boyer-Moore voting finds the element that appears more than n/2 times.

## Steps

1. Keep a candidate and a count.
2. When the count is zero, adopt the current value as candidate.
3. Increment for matches and decrement for mismatches.
4. The majority element survives as the final candidate.
5. Return that candidate.
