// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        if (matrix.isEmpty() || matrix[0].isEmpty()) {
            return false
        }
        var row = 0
        var col = matrix[0].size - 1
        while (row < matrix.size && col >= 0) {
            val value = matrix[row][col]
            when {
                value == target -> return true
                value > target -> col--
                else -> row++
            }
        }
        return false
    }
}
