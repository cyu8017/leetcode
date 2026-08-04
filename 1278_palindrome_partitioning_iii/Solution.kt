// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

class Solution {
    fun palindromePartition(s: String, k: Int): Int {
        val n = s.length
        val cost = Array(n) { IntArray(n) }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                cost[i][j] = (if (length > 2) cost[i + 1][j - 1] else 0) + if (s[i] != s[j]) 1 else 0
            }
        }
        val inf = n + 1
        val dp = Array(k + 1) { IntArray(n + 1) { inf } }
        dp[0][0] = 0
        for (parts in 1..k) {
            for (end in parts..n) {
                for (start in parts - 1 until end) {
                    dp[parts][end] = minOf(dp[parts][end], dp[parts - 1][start] + cost[start][end - 1])
                }
            }
        }
        return dp[k][n]
    }
}
