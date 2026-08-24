// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
    fun maxMoves(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var dp = IntArray(m)
        for (c in n - 2 downTo 0) {
            val ndp = IntArray(m)
            for (r in 0 until m) {
                var best = 0
                for (dr in -1..1) {
                    val nr = r + dr
                    if (nr in 0 until m && grid[nr][c + 1] > grid[r][c])
                        best = maxOf(best, 1 + dp[nr])
                }
                ndp[r] = best
            }
            dp = ndp
        }
        var ans = 0
        for (v in dp) ans = maxOf(ans, v)
        return ans
    }
}
