// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

class Solution {
    fun minChanges(nums: IntArray, k: Int): Int {
        val freq = Array(k) { IntArray(1024) }
        val size = IntArray(k)
        for (i in nums.indices) {
            freq[i % k][nums[i]]++
            size[i % k]++
        }
        val inf = 1_000_000_000
        var dp = IntArray(256) { inf }
        dp[0] = 0
        for (i in 0 until k) {
            val ndp = IntArray(256) { inf }
            for (xv in 0 until 256) {
                val cost = size[i] - freq[i][xv]
                for (xo in 0 until 256) {
                    if (dp[xo] == inf) {
                        continue
                    }
                    val key = xo xor xv
                    if (dp[xo] + cost < ndp[key]) {
                        ndp[key] = dp[xo] + cost
                    }
                }
            }
            dp = ndp
        }
        return dp[0]
    }
}
