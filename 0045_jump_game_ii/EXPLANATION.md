# How We Solve Jump Game II

Jump from index 0 to the end in the fewest jumps. Each step you can jump up to nums[i].

## Steps

1. Track the farthest index you can reach.
2. Track the end of the current jump window.
3. Walk index by index (stop before the last spot).
4. Update farthest with i + nums[i].
5. When you hit the window end, count one jump and open a new window at farthest.
6. Return the jump count.
