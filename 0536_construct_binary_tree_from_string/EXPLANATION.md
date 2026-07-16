# How We Solve Construct Binary Tree from String

The string uses nested parentheses for left and right children.

## Steps

1. Parse the signed integer at the current position.
2. If `(` follows, recursively build the left subtree and consume `)`.
3. Repeat for the right subtree when another `(` appears.
