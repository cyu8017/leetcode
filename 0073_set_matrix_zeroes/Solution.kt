// LeetCode 0073 - Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

class Solution {
    fun setZeroes(matrix: Array<IntArray>) {
        val rows = matrix.size
        val cols = matrix[0].size
        val firstRowZero = matrix[0].any { it == 0 }
        val firstColZero = matrix.any { it[0] == 0 }

        for (i in 1 until rows) {
            for (j in 1 until cols) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }

        for (i in 1 until rows) {
            for (j in 1 until cols) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0
                }
            }
        }

        if (firstRowZero) {
            for (j in 0 until cols) {
                matrix[0][j] = 0
            }
        }
        if (firstColZero) {
            for (i in 0 until rows) {
                matrix[i][0] = 0
            }
        }
    }
}
