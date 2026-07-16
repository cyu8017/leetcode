# How We Solve Basic Calculator III

Recursive stack parser for `+ - * /` with parentheses; division truncates toward zero.

## Steps

1. Scan numbers and operators; recurse on `(...)`.
2. Apply `*`/`/` immediately on the stack; defer `+`/`-` as signed values.
3. Sum the stack when a subexpression ends.
