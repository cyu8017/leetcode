// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

class Solution {
    fun countOfArrays(n: Int, m: Int, k: Int): Int {
        val mod = 1000000007
        val even = m / 2
        val odd = m - even
        val dp = Array(n + 1) { Array(k + 1) { IntArray(2) } }
        dp[1][0][0] = odd
        dp[1][0][1] = even
        for (i in 1 until n) {
            for (j in 0..k) {
                dp[i + 1][j][0] = (dp[i + 1][j][0] + (((dp[i][j][0].toLong() + dp[i][j][1]) % mod) * odd % mod).toInt()) % mod
                dp[i + 1][j][1] = (dp[i + 1][j][1] + (dp[i][j][0].toLong() * even % mod).toInt()) % mod
                if (j < k) {
                    dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + (dp[i][j][1].toLong() * even % mod).toInt()) % mod
                }
            }
        }
        return (dp[n][k][0] + dp[n][k][1]) % mod
    }
}
