# How We Solve Repeated DNA Sequences

Slide a 10-letter window and record sequences seen more than once.

## Steps

1. Walk every substring of length 10.
2. Track sequences already seen in a set.
3. When a sequence appears again, add it to the result set.
4. Deduplicate automatically with the result set.
5. Return the collected sequences.
