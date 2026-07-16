# How We Solve Valid Parenthesis String

Track the possible open-count range as `*` flexes between `(`, `)`, or empty.

## Steps

1. Maintain low/high bounds on unmatched opens.
2. `(` raises both; `)` lowers both (clamp low at 0); `*` widens the range.
3. Fail if high goes negative; succeed if low ends at 0.
