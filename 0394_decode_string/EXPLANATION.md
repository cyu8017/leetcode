# How We Solve Decode String

A stack stores unfinished prefixes and repeat counts around brackets.

## Steps

1. Accumulate digits into the current repeat count.
2. On '[', push the current string and count, then reset.
3. On ']', pop and expand the decoded segment by the saved count.
