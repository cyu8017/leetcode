// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

class Solution {
    fun numMagicSquaresInside(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        if (rows < 3 || cols < 3) return 0
        var ans = 0
        for (i in 0 until rows - 2) {
            for (j in 0 until cols - 2) {
                if (magic(grid, i, j)) ans++
            }
        }
        return ans
    }

    private fun magic(a: Array<IntArray>, r: Int, c: Int): Boolean {
        val vals = IntArray(9)
        var k = 0
        for (i in 0 until 3) {
            for (j in 0 until 3) vals[k++] = a[r + i][c + j]
        }
        vals.sort()
        for (i in 0 until 9) if (vals[i] != i + 1) return false
        return a[r][c] + a[r][c + 1] + a[r][c + 2] == 15
            && a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15
            && a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c] + a[r + 2][c] == 15
            && a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15
            && a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15
    }
}
