# How We Solve Sliding Window Maximum

Maintain a deque of indices with decreasing values.

## Steps

1. Append each index to the deque after removing smaller tail values.
2. Remove indices that fall outside the current window.
3. Once the window is full, the deque front is the maximum index.
4. Append that maximum to the answer.
5. Continue until the end of the array.
