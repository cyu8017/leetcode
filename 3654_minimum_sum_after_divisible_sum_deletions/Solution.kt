// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

class Solution {
    fun minArraySum(nums: IntArray, k: Int): Long {
        val n = nums.size
        val prefix = IntArray(n + 1)
        for (i in 0 until n) prefix[i + 1] = (prefix[i] + nums[i]) % k
        val inf = 1L shl 62
        val dp = LongArray(n + 1)
        val best = LongArray(k) { inf }
        best[0] = 0
        for (i in 1..n) {
            dp[i] = dp[i - 1] + nums[i - 1]
            if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]]
            if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i]
        }
        return dp[n]
    }
}
