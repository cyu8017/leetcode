// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution {
    fun minOperations(grid: Array<IntArray>, x: Int): Int {
var vals: MutableList<Int> = mutableListOf()
var bas: Int = grid[0][0] % x
for (row in grid) {
for (v in row) {
if (v % x != bas) {
return -1
}
vals.add(v)
}
}
vals.sort()
var median: Int = vals[vals.size / 2], ans = 0
for (v in vals) {
ans += kotlin.math.abs(v - median) / x
}
return ans
}
}
