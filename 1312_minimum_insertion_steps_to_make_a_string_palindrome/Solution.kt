// LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution {
    fun minInsertions(s: String): Int {
        val n = s.length
        val dp = IntArray(n)
        for (left in n - 2 downTo 0) {
            var diagonal = 0
            for (right in left + 1 until n) {
                val old = dp[right]
                dp[right] = if (s[left] == s[right]) diagonal else 1 + minOf(dp[right], dp[right - 1])
                diagonal = old
            }
        }
        return if (dp.isEmpty()) 0 else dp[n - 1]
    }
}
