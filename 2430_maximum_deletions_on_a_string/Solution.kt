// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution {
    fun deleteString(s: String): Int {
        val n = s.length
        val lcp = Array(n + 1) { IntArray(n + 1) }
        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (s[i] == s[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1
            }
        }
        val dp = IntArray(n)
        for (i in n - 1 downTo 0) {
            dp[i] = 1
            var len = 1
            while (i + 2 * len <= n) {
                if (lcp[i][i + len] >= len) dp[i] = maxOf(dp[i], 1 + dp[i + len])
                len++
            }
        }
        return dp[0]
    }
}
