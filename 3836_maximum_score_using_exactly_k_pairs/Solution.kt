// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

class Solution {
    fun maxScore(nums1: IntArray, nums2: IntArray, K: Int): Long {
        val n = nums1.size
        val m = nums2.size
        val NEG = Long.MIN_VALUE / 4
        val f = Array(n + 1) { Array(m + 1) { LongArray(K + 1) { NEG } } }
        f[0][0][0] = 0
        for (i in 0..n) {
            for (j in 0..m) {
                for (k in 0..K) {
                    if (i > 0) f[i][j][k] = maxOf(f[i][j][k], f[i - 1][j][k])
                    if (j > 0) f[i][j][k] = maxOf(f[i][j][k], f[i][j - 1][k])
                    if (i > 0 && j > 0 && k > 0) {
                        f[i][j][k] = maxOf(f[i][j][k], f[i - 1][j - 1][k - 1] + nums1[i - 1].toLong() * nums2[j - 1])
                    }
                }
            }
        }
        return f[n][m][K]
    }
}
