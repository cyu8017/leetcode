// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

class Solution {
    fun rotate(matrix: Array<IntArray>) {
        val n = matrix.size

        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            }
        }

        for (row in matrix) {
            row.reverse()
        }
    }
}
