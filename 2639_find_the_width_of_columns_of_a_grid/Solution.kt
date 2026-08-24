// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    fun findColumnWidth(grid: Array<IntArray>): IntArray {
        val n = grid[0].size
        val ans = IntArray(n)
        for (row in grid) {
            for (j in 0 until n) {
                val w = width(row[j])
                if (w > ans[j]) ans[j] = w
            }
        }
        return ans
    }

    private fun width(x0: Int): Int {
        if (x0 == 0) return 1
        var x = x0
        var w = 0
        if (x < 0) {
            w++
            x = -x
        }
        while (x > 0) {
            w++
            x /= 10
        }
        return w
    }
}
