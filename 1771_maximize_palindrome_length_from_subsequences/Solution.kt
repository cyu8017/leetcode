// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

class Solution {
    fun longestPalindrome(word1: String, word2: String): Int {
        val s = word1 + word2
        val n = s.length
        val n1 = word1.length
        val dp = Array(n) { IntArray(n) }
        var ans = 0
        for (i in n - 1 downTo 0) {
            dp[i][i] = 1
            for (j in i + 1 until n) {
                if (s[i] == s[j]) {
                    dp[i][j] = if (j == i + 1) 2 else dp[i + 1][j - 1] + 2
                    if (i < n1 && n1 <= j) {
                        ans = maxOf(ans, dp[i][j])
                    }
                } else {
                    dp[i][j] = maxOf(dp[i + 1][j], dp[i][j - 1])
                }
            }
        }
        return ans
    }
}
