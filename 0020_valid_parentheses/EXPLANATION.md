# How We Solve Valid Parentheses

Check if brackets match: (), [], {}.

## Steps

1. Use a stack (a pile you only touch on top).
2. For an open bracket, push it on the pile.
3. For a close bracket, pop and check it matches the opener.
4. If pile is empty when you need to pop, it is invalid.
5. At the end, pile must be empty.
6. Return true or false.
