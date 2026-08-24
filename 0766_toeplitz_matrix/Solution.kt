// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

class Solution {
    fun isToeplitzMatrix(matrix: Array<IntArray>): Boolean {
        for (r in 1 until matrix.size) {
            for (c in 1 until matrix[0].size) {
                if (matrix[r][c] != matrix[r - 1][c - 1]) return false
            }
        }
        return true
    }
}
