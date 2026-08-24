// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution {
    fun minimumArea(grid: Array<IntArray>): Int {
        var x1 = grid.size
        var y1 = grid[0].size
        var x2 = 0
        var y2 = 0
        for (i in 0 until grid.size) {
            for (j in 0 until grid[0].size) {
                if (grid[i][j] == 1) {
                    x1 = minOf(x1, i); y1 = minOf(y1, j)
                    x2 = maxOf(x2, i); y2 = maxOf(y2, j)
                }
            }
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1)
    }
}
