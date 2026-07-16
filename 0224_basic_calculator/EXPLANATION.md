# How We Solve Basic Calculator

Evaluate expressions with `+`, `-`, and parentheses using a stack.

## Steps

1. Walk the string while tracking the current number and sign.
2. On `+` or `-`, apply the current sign to the running result.
3. On `(`, push the current result and sign onto a stack.
4. On `)`, finish the inner result and combine it with the stack.
5. Add the final number after the loop ends.
