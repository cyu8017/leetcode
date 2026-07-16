# How We Solve Count The Repetitions

Simulate matching `s2` inside repeated `s1`, then detect cycles to skip bulk repetitions.

## Steps

1. Walk through `n1` copies of `s1`, counting full matches of `s2`.
2. Record `(s2 index, match count)` when a repeat position revisits.
3. Jump ahead using the detected cycle and divide by `n2`.
