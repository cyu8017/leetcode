// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

class Solution {
    fun gridGame(grid: Array<IntArray>): Long {
var n: Int = grid[0].size
var top: Long = 0
var bottom: Long = 0
var ans: Long = Long.MAX_VALUE
for (v in grid[0]) {
top += v
}
for (i in 0 until n) {
top -= grid[0][i]
ans = minOf(ans, maxOf(top, bottom))
bottom += grid[1][i]
}
return ans
}
}
