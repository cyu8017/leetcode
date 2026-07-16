# How We Solve Basic Calculator II

Use a stack to defer addition and subtraction while handling `*` and `/` immediately.

## Steps

1. Parse numbers and operators left to right.
2. Push signed values for `+` and `-`.
3. Multiply or divide with the top stack value for `*` and `/`.
4. Reset the current number after each operator.
5. Return the sum of the stack.
