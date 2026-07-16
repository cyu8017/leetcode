# 3991. Sort Array Using Prefix Reversals

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/sort-array-using-prefix-reversals/](https://leetcode.com/problems/sort-array-using-prefix-reversals/)

You are given a permutation `nums` of `0..n-1` and an array `pre` of allowed prefix lengths. In one operation you may pick any length `i` from `pre` and reverse the prefix `nums[0..i-1]`. Return the minimum number of operations needed to sort `nums` in increasing order, or `-1` if it is impossible.

## Approach

Breadth-first search over permutation states.

- Each state is the current arrangement of the array (stored as a tuple so it is hashable).
- From a state, one move per allowed prefix length `i` produces the neighbor `reversed(prefix of i) + rest`. Lengths below 2 are no-ops and are skipped.
- BFS from the starting permutation guarantees the first time we reach the sorted permutation `(0, 1, ..., n-1)` we have used the minimum number of reversals. If BFS exhausts all reachable states, return `-1`.

Since `nums` is a permutation of a small `n`, the state space is at most `n!`, giving time `O(n! * n * m)` and space `O(n! * n)` where `m = len(pre)`.

### Examples

- `nums = [2,0,1], pre = [2,3]` → `2` (reverse prefix 3 to get `[1,0,2]`, then prefix 2 to get `[0,1,2]`)
- `nums = [1,0,2], pre = [1,3]` → `-1` (only `[1,0,2]` and `[2,0,1]` are reachable)
- `nums = [0,1], pre = [2]` → `0` (already sorted)
