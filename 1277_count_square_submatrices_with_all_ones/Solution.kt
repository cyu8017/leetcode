// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    fun countSquares(matrix: Array<IntArray>): Int {
        var answer = 0
        for (r in matrix.indices) {
            for (c in matrix[0].indices) {
                if (matrix[r][c] != 0 && r > 0 && c > 0) {
                    matrix[r][c] += minOf(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                }
                answer += matrix[r][c]
            }
        }
        return answer
    }
}
