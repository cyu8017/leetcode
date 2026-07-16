# How We Solve Evaluate Reverse Polish Notation

Use a stack: push numbers, pop two operands for each operator.

## Steps

1. Scan tokens left to right.
2. Push integers onto the stack.
3. For an operator, pop right then left.
4. Apply the operator (division truncates toward zero) and push the result.
5. The final stack value is the answer.
