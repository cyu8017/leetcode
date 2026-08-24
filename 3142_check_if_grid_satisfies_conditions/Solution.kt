// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution {
    fun satisfiesConditions(grid: Array<IntArray>): Boolean {
        var m = grid.size
        var n = grid[0].size
        for (i in 0 until m) {
            for (j in 0 until n) {
                var x = grid[i][j]
                if (i + 1 < m && x != grid[i + 1][j]) return false
                if (j + 1 < n && x == grid[i][j + 1]) return false
            }
        }
        return true
    }
}
