// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution {
    fun reverseSubmatrix(grid: Array<IntArray>, x: Int, y: Int, k: Int): Array<IntArray> {
        for (i in x until x + k / 2) {
            var i2 = x + k - 1 - (i - x)
            for (j in y until y + k) {
                var tmp = grid[i][j]
                grid[i][j] = grid[i2][j]
                grid[i2][j] = tmp
            }
        }
        return grid
    }
}
