// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

class Solution {
    fun minExtraChar(s: String, dictionary: Array<String>): Int {
        val dict = dictionary.toHashSet()
        val n = s.length
        val dp = IntArray(n + 1) { n }
        dp[0] = 0
        for (i in 0 until n) {
            dp[i + 1] = minOf(dp[i + 1], dp[i] + 1)
            for (j in i + 1..n) {
                if (s.substring(i, j) in dict) dp[j] = minOf(dp[j], dp[i])
            }
        }
        return dp[n]
    }
}
