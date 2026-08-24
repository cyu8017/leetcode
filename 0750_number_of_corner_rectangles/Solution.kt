// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

class Solution {
    fun countCornerRectangles(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        var ans = 0
        for (i in 0 until m) {
            for (j in i + 1 until m) {
                var count = 0
                for (c in 0 until n) { if (grid[i][c] == 1 && grid[j][c] == 1) count++ }
                ans += count * (count - 1) / 2
            }
        }
        return ans
    }
}
