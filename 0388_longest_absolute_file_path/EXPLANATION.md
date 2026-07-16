# How We Solve Longest Absolute File Path

Tab depth tracks directory prefixes on a stack.

## Steps

1. Parse each line and measure depth by tab count.
2. Pop stack until depth matches; directories extend prefix length.
3. For files, add name length to current prefix and track the maximum.
