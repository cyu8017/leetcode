// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

class Solution {
    fun longestSubsequence(nums: IntArray): Int {
        var n = nums.size
        var ans = 1
        var dp = Array(n) { IntArray(301) }
        for (i in 0 until n) {
            for (j in 0 until i) {
                var d = kotlin.math.abs(nums[i] - nums[j])
                var best = 1
                for (pd in d .. 300) {
                    if (dp[j][pd] > best) best = dp[j][pd]
                }
                if (best + 1 > dp[i][d]) dp[i][d] = best + 1
                if (dp[i][d] > ans) ans = dp[i][d]
            }
            if (dp[i][0] < 1) dp[i][0] = 1
        }
        return ans
    }
}
