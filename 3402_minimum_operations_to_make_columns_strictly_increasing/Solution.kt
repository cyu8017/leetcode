// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

class Solution {
    fun minimumOperations(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        var ans = 0
        for (j in 0 until n) {
            for (i in 1 until m) {
                if (grid[i][j] <= grid[i - 1][j]) {
                    var need = grid[i - 1][j] + 1
                    ans += need - grid[i][j]
                    grid[i][j] = need
                }
            }
        }
        return ans
    }
}
