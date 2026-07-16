// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
    fun longestPalindromeSubseq(s: String): Int {
        val length = s.length
        val dp = Array(length) { IntArray(length) }
        for (index in length - 1 downTo 0) {
            dp[index][index] = 1
            for (end in index + 1 until length) {
                dp[index][end] = if (s[index] == s[end]) {
                    dp[index + 1][end - 1] + 2
                } else {
                    maxOf(dp[index + 1][end], dp[index][end - 1])
                }
            }
        }
        return dp[0][length - 1]
    }
}
