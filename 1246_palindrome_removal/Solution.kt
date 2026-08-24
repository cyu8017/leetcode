// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

class Solution {
    fun minimumMoves(arr: IntArray): Int {
        val n = arr.size
        val dp = Array(n) { IntArray(n) }
        for (i in 0 until n) dp[i][i] = 1
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                dp[i][j] = 1 + dp[i + 1][j]
                if (arr[i] == arr[i + 1]) {
                    dp[i][j] = minOf(dp[i][j], 1 + if (i + 2 <= j) dp[i + 2][j] else 0)
                }
                for (k in i + 2..j) {
                    if (arr[i] == arr[k]) {
                        dp[i][j] = minOf(dp[i][j], dp[i + 1][k - 1] + if (k < j) dp[k + 1][j] else 0)
                    }
                }
            }
        }
        return dp[0][n - 1]
    }
}
