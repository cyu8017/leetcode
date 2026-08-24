// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/


class Solution {
    fun lengthOfLongestSubsequence(nums: List<Int>, target: Int): Int {
        val dp = IntArray(target + 1) { -1 }
        dp[0] = 0
        for (v in nums) {
            for (s in target downTo v) {
                if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1
            }
        }
        return dp[target]
    }
}
