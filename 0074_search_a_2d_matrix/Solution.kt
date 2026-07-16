// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        var row = 0
        var col = matrix[0].size - 1

        while (row < matrix.size && col >= 0) {
            when {
                matrix[row][col] == target -> return true
                matrix[row][col] > target -> col--
                else -> row++
            }
        }

        return false
    }
}
