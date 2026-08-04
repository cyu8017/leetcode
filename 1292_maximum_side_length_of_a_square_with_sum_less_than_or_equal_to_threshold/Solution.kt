// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution {
    fun maxSideLength(mat: Array<IntArray>, threshold: Int): Int {
        val m = mat.size
        val n = mat[0].size
        val prefix = Array(m + 1) { IntArray(n + 1) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
            }
        }
        var lo = 0
        var hi = minOf(m, n)
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (possible(prefix, m, n, mid, threshold)) lo = mid else hi = mid - 1
        }
        return lo
    }

    private fun possible(prefix: Array<IntArray>, m: Int, n: Int, size: Int, threshold: Int): Boolean {
        for (r in size..m) {
            for (c in size..n) {
                val sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size]
                if (sum <= threshold) return true
            }
        }
        return false
    }
}
