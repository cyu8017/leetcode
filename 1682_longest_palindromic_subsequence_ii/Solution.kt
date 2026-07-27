// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

class Solution {
    fun longestPalindromeSubseq(s: String): Int {
        val n = s.length
        val dp = Array(n) { Array(n) { IntArray(26) } }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                for (c in 0 until 26) {
                    dp[i][j][c] = maxOf(dp[i + 1][j][c], dp[i][j - 1][c])
                }
                if (s[i] == s[j]) {
                    val c = s[i] - 'a'
                    var inner = 0
                    if (length > 2) {
                        for (x in 0 until 26) {
                            if (x != c) inner = maxOf(inner, dp[i + 1][j - 1][x])
                        }
                    }
                    dp[i][j][c] = maxOf(dp[i][j][c], inner + 2)
                }
            }
        }
        return dp[0][n - 1].maxOrNull() ?: 0
    }
}
