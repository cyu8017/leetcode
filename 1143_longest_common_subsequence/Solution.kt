// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    fun longestCommonSubsequence(text1: String, text2: String): Int {
        val m = text1.length
        val n = text2.length
        val dp = IntArray(n + 1)
        for (i in 1..m) {
            var prev = 0
            for (j in 1..n) {
                val cur = dp[j]
                if (text1[i - 1] == text2[j - 1]) dp[j] = prev + 1
                else dp[j] = maxOf(dp[j], dp[j - 1])
                prev = cur
            }
        }
        return dp[n]
    }
}
