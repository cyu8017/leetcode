# How We Solve Parse Lisp Expression

Recursive-descent evaluate `let` / `add` / `mult` with nested scopes.

## Steps

1. Tokenize on parentheses and whitespace.
2. `let` binds variables in a new scope until the final expression.
3. `add`/`mult` evaluate two operands and return the result.
