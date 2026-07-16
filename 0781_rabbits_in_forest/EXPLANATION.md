# How We Solve Rabbits in Forest

Rabbits answering `x` must form groups of size `x+1`.

## Steps

1. Count how many rabbits gave each answer.
2. For answer `x`, pack them into groups of size `x+1`.
3. Sum `ceil(count / (x+1)) * (x+1)` over all answers.
