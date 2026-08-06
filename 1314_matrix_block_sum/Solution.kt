// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

class Solution {
    fun matrixBlockSum(mat: Array<IntArray>, k: Int): Array<IntArray> {
        val m = mat.size
        val n = mat[0].size
        val prefix = Array(m + 1) { IntArray(n + 1) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
            }
        }
        val answer = Array(m) { IntArray(n) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                val r1 = maxOf(0, r - k)
                val c1 = maxOf(0, c - k)
                val r2 = minOf(m, r + k + 1)
                val c2 = minOf(n, c + k + 1)
                answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
            }
        }
        return answer
    }
}
