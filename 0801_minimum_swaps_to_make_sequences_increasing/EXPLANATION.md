# How We Solve Minimum Swaps To Make Sequences Increasing

DP whether index `i` is swapped or not, keeping both sequences strictly increasing.

## Steps

1. `keep[i]` / `swap[i]` = min swaps ending without / with a swap at `i`.
2. If both pairs already increase, inherit the matching previous state.
3. If crossed values increase, allow transitioning between swap and keep.
