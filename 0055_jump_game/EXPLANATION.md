# How We Solve Jump Game

Check if you can reach the last index by jumping from each spot.

## Steps

1. Keep track of the farthest index you can reach so far.
2. Walk through each index in order.
3. If the current index is beyond the farthest reach, return false.
4. Update the farthest reach using the current jump length.
5. If you can visit every index, return true.
