// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

class Solution {
    private fun count(g: Array<IntArray>): Int {
var m: Int = g.size
var n: Int = g[0].size
var dp: Array<IntArray> = IntArray(m)[]
for (i in 0 until m) {
dp[i] = IntArray(n)
for (j in 0 until n) {
dp[i][j] = g[i][j]
}
}
var ans: Int = 0
for (i in m - 2 downTo 0) {
for (j in 1 until n - 1) {
if (g[i][j] == 1) {
dp[i][j] = 1 + minOf(dp[i + 1][j - 1], minOf(dp[i + 1][j], dp[i + 1][j + 1]))
ans += dp[i][j] - 1
}
}
}
return ans
}

    fun countPyramids(grid: Array<IntArray>): Int {
var ans: Int = count(grid)
var m: Int = grid.size
var rev: Array<IntArray> = IntArray(m)[]
for (i in 0 until m) {
rev[i] = grid[m - 1 - i]
}
return ans + count(rev)
}
}
