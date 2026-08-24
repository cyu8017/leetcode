// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

class Solution {
    fun checkXMatrix(grid: Array<IntArray>): Boolean {
        val n = grid.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                val diag = i == j || i + j == n - 1
                if (diag) {
                    if (grid[i][j] == 0) return false
                } else if (grid[i][j] != 0) return false
            }
        }
        return true
    }
}
