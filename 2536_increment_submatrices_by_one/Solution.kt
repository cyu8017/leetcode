// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

class Solution {
    fun rangeAddQueries(n: Int, queries: Array<IntArray>): Array<IntArray> {
        val diff = Array(n + 1) { IntArray(n + 1) }
        for (q in queries) {
            val r1 = q[0]; val c1 = q[1]; val r2 = q[2]; val c2 = q[3]
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        }
        val mat = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                var v = diff[i][j]
                if (i > 0) v += mat[i - 1][j]
                if (j > 0) v += mat[i][j - 1]
                if (i > 0 && j > 0) v -= mat[i - 1][j - 1]
                mat[i][j] = v
            }
        }
        return mat
    }
}
