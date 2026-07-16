# How We Solve Majority Element II

Boyer-Moore voting with two candidates finds elements appearing more than n/3 times.

## Steps

1. First pass tracks two candidate values with counters.
2. Replace empty counters with new values.
3. Decrement both counters when neither candidate matches.
4. Second pass counts actual frequencies of the candidates.
5. Keep values whose counts exceed `n // 3`.
