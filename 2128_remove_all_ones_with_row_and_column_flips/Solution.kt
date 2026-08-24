// LeetCode 2128 - Remove All Ones With Row and Column Flips
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

class Solution {
    fun removeOnes(grid: Array<IntArray>): Boolean {
        var m: Int = grid.size, n = grid[0].size
        for (i in 1 until m) {
            var same: Boolean = grid[i][0] == grid[0][0]
            for (j in 0 until n) {
                if ((grid[i][j] == grid[0][j]) != same) return false
            }
        }
        return true
    }
}
