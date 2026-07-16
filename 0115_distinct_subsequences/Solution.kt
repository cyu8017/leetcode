// LeetCode 0115 - Distinct Subsequences
// https://leetcode.com/problems/distinct-subsequences/

class Solution {
    fun numDistinct(s: String, t: String): Int {
        val dp = LongArray(t.length + 1)
        dp[0] = 1
        for (ch in s) {
            for (j in t.length downTo 1) {
                if (ch == t[j - 1]) dp[j] += dp[j - 1]
            }
        }
        return dp[t.length].toInt()
    }
}