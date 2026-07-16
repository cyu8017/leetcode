# How We Solve Rotate Array

Three reverses rotate the array right by `k` in place.

## Steps

1. Reduce `k` modulo the array length.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining suffix.
5. The array is now rotated right by `k`.
