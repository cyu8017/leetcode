# How We Solve Sum Root to Leaf Numbers

Each root-to-leaf path forms a decimal number; sum them all.

## Steps

1. DFS with the number built so far.
2. Append the current digit by multiplying by 10 and adding `val`.
3. At a leaf, return that number.
4. Otherwise return the sum of left and right recursive results.
5. Start the DFS from the root with 0.
