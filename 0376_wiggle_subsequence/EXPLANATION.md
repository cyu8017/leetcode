# How We Solve Wiggle Subsequence

Track longest wiggle ending up or ending down.

## Steps

1. Start up and down lengths at 1.
2. Extend up when the current value rises from the previous.
3. Extend down when it falls; return the maximum length.
