# How We Solve Count and Say

Each term describes the previous term (run-length encoding). n=1 -> "1", n=2 -> "11", etc.

## Steps

1. Start with term = "1".
2. For each step until n, build the next term.
3. Walk the current term and count same digits in a row.
4. Write count + digit for each group.
5. That new string becomes the next term.
6. Return the final term.
