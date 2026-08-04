// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

class Solution {
    fun isValidPalindrome(s: String, k: Int): Boolean {
        val n = s.length
        val dp = IntArray(n)
        for (i in n - 1 downTo 0) {
            var previous = 0
            for (j in i + 1 until n) {
                val old = dp[j]
                if (s[i] == s[j]) dp[j] = previous
                else dp[j] = 1 + minOf(dp[j], dp[j - 1])
                previous = old
            }
        }
        return n == 0 || dp[n - 1] <= k
    }
}
