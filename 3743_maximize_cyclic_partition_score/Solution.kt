// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize_cyclic_partition_score/

class Solution {
    fun maximumScore(nums: IntArray, k0: Int): Long {
        val n = nums.size
        var k = k0
        val a = IntArray(n * 2)
        System.arraycopy(nums, 0, a, 0, n)
        System.arraycopy(nums, 0, a, n, n)
        if (k > n) k = n
        var best = 0L
        val NEG = -(1L shl 60)
        for (start in 0 until n) {
            val seg = a.copyOfRange(start, start + n)
            val dp = Array(n + 1) { LongArray(k + 1) { NEG } }
            dp[0][0] = 0
            for (i in 1..n) {
                for (j in 1..minOf(k, i)) {
                    var mx = NEG
                    for (t in i downTo j) {
                        if (seg[t - 1] > mx) mx = seg[t - 1].toLong()
                        if (dp[t - 1][j - 1] > NEG) {
                            val cand = dp[t - 1][j - 1] + mx
                            if (cand > dp[i][j]) dp[i][j] = cand
                        }
                    }
                }
            }
            if (dp[n][k] > best) best = dp[n][k]
        }
        return best
    }
}
