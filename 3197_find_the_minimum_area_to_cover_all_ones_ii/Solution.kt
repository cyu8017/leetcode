// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

class Solution {
    fun minimumSum(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        var ans = m * n
        for (i1 in 0 until m - 1) {
            for (i2 in i1 + 1 until m - 1) {
                ans = minOf(ans, area(grid, 0, 0, i1, n - 1) + area(grid, i1 + 1, 0, i2, n - 1) + area(grid, i2 + 1, 0, m - 1, n - 1))
            }
        }
        for (j1 in 0 until n - 1) {
            for (j2 in j1 + 1 until n - 1) {
                ans = minOf(ans, area(grid, 0, 0, m - 1, j1) + area(grid, 0, j1 + 1, m - 1, j2) + area(grid, 0, j2 + 1, m - 1, n - 1))
            }
        }
        for (i in 0 until m - 1) {
            for (j in 0 until n - 1) {
                ans = minOf(ans, area(grid, 0, 0, i, j) + area(grid, 0, j + 1, i, n - 1) + area(grid, i + 1, 0, m - 1, n - 1))
                ans = minOf(ans, area(grid, 0, 0, i, n - 1) + area(grid, i + 1, 0, m - 1, j) + area(grid, i + 1, j + 1, m - 1, n - 1))
                ans = minOf(ans, area(grid, 0, 0, i, j) + area(grid, i + 1, 0, m - 1, j) + area(grid, 0, j + 1, m - 1, n - 1))
                ans = minOf(ans, area(grid, 0, 0, m - 1, j) + area(grid, 0, j + 1, i, n - 1) + area(grid, i + 1, j + 1, m - 1, n - 1))
            }
        }
        return ans
    }

    private fun area(grid: Array<IntArray>, i1: Int, j1: Int, i2: Int, j2: Int): Int {
        val inf = Int.MAX_VALUE / 4
        var x1 = inf
        var y1 = inf
        var x2 = -inf
        var y2 = -inf
        for (i in i1 ..i2) {
            for (j in j1 ..j2) {
                if (grid[i][j] == 1) {
                    x1 = minOf(x1, i)
                    y1 = minOf(y1, j)
                    x2 = maxOf(x2, i)
                    y2 = maxOf(y2, j)
                }
            }
        }
        if (x1 == inf) {
            return 0
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1)
    }
}
