// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution {
    fun areSimilar(mat: Array<IntArray>, k: Int): Boolean {
        val m = mat.size
        val n = mat[0].size
        for (i in 0 until m) {
            val shift = if (i % 2 == 0) {
                var s = n - (k % n)
                if (s == n) 0 else s
            } else {
                k % n
            }
            for (j in 0 until n) {
                if (mat[i][j] != mat[i][(j + shift) % n]) return false
            }
        }
        return true
    }
}
