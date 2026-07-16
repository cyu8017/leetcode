# How We Solve Magical String

Generate the self-describing sequence and count ones in the first n characters.

## Steps

1. Start from `[1, 2, 2]` and read counts from index 2 onward.
2. Append one or two alternating values (1/2) according to each count.
3. Return how many `1`s appear in the first `n` elements.
