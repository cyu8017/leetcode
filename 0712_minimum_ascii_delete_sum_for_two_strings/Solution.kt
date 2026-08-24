// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution {
    fun minimumDeleteSum(s1: String, s2: String): Int {
        var m = s1.length
        var n = s2.length
        var dp = Array(m + 1) { IntArray(n + 1) }
        for (i in 1 ..m) { dp[i][0] = dp[i - 1][0] + s1[i - 1] }
        for (j in 1 ..n) { dp[0][j] = dp[0][j - 1] + s2[j - 1] }
        for (i in 1 ..m) {
            for (j in 1 ..n) {
                if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1]
                else dp[i][j] = minOf(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1])
            }
        }
        return dp[m][n]
    }
}
