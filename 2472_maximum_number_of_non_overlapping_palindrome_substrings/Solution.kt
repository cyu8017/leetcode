// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution {
    fun maxPalindromes(s: String, k: Int): Int {
        val n = s.length
        val isPal = Array(n) { BooleanArray(n) }
        for (i in 0 until n) isPal[i][i] = true
        for (i in 0 until n - 1) isPal[i][i + 1] = s[i] == s[i + 1]
        for (length in 3..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                isPal[i][j] = s[i] == s[j] && isPal[i + 1][j - 1]
            }
        }
        val dp = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            dp[i] = dp[i + 1]
            for (j in i + k - 1 until n) {
                if (isPal[i][j] && 1 + dp[j + 1] > dp[i]) dp[i] = 1 + dp[j + 1]
            }
        }
        return dp[0]
    }
}
