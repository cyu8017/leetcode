# How We Solve Score of Parentheses

Stack scores: `()` is 1, and nesting doubles the inner score.

## Steps

1. Push a new frame on `(`.
2. On `)`, pop the inner score and add `max(2*inner, 1)` to the parent.
3. The root frame holds the total.
