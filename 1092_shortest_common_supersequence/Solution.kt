// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

class Solution {
    fun shortestCommonSupersequence(str1: String, str2: String): String {
        val m = str1.length
        val n = str2.length
        val dp = Array(m + 1) { IntArray(n + 1) }
        for (i in 1..m) {
            for (j in 1..n) {
                dp[i][j] = if (str1[i - 1] == str2[j - 1]) {
                    dp[i - 1][j - 1] + 1
                } else {
                    maxOf(dp[i - 1][j], dp[i][j - 1])
                }
            }
        }
        var i = m
        var j = n
        val chars = StringBuilder()
        while (i > 0 && j > 0) {
            when {
                str1[i - 1] == str2[j - 1] -> {
                    chars.append(str1[i - 1])
                    i--
                    j--
                }
                dp[i - 1][j] >= dp[i][j - 1] -> {
                    chars.append(str1[i - 1])
                    i--
                }
                else -> {
                    chars.append(str2[j - 1])
                    j--
                }
            }
        }
        while (i > 0) {
            chars.append(str1[i - 1])
            i--
        }
        while (j > 0) {
            chars.append(str2[j - 1])
            j--
        }
        return chars.reverse().toString()
    }
}
