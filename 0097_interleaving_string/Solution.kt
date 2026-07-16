// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

class Solution {
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        if (s1.length + s2.length != s3.length) {
            return false
        }

        val m = s1.length
        val n = s2.length
        val dp = BooleanArray(n + 1)
        dp[0] = true

        for (j in 1..n) {
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1]
        }

        for (i in 1..m) {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1]
            for (j in 1..n) {
                dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1]) ||
                    (dp[j - 1] && s2[j - 1] == s3[i + j - 1])
            }
        }

        return dp[n]
    }
}
