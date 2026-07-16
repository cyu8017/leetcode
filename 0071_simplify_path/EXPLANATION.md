# How We Solve Simplify Path

Turn a Unix-style path into its shortest absolute form.

## Steps

1. Split the path by `/`.
2. Skip empty parts and `.`.
3. On `..`, pop the last folder if the stack is not empty.
4. Otherwise push the folder name.
5. Join with `/` and put a `/` at the front.
