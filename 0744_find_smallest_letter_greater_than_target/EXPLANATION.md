# How We Solve Find Smallest Letter Greater Than Target

Binary search for the first letter strictly greater than `target` (circular).

## Steps

1. Search the sorted `letters` array.
2. Land on the insertion point after all `<= target`.
3. Wrap with modulo to handle the circular alphabet.
