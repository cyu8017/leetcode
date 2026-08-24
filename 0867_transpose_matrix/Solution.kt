// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

class Solution {
    fun transpose(matrix: Array<IntArray>): Array<IntArray> {
        val m = matrix.size
        val n = matrix[0].size
        val ans = Array(n) { IntArray(m) }
        for (i in 0 until m) {
            for (j in 0 until n) ans[j][i] = matrix[i][j]
        }
        return ans
    }
}
