// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

class Solution {
    fun sellingWood(m: Int, n: Int, prices: Array<IntArray>): Long {
        val price = Array(m + 1) { LongArray(n + 1) }
        val dp = Array(m + 1) { LongArray(n + 1) }
        for (p in prices) price[p[0]][p[1]] = p[2].toLong()
        for (h in 1..m) {
            for (w in 1..n) {
                var best = price[h][w]
                for (i in 1 until h) best = maxOf(best, dp[i][w] + dp[h - i][w])
                for (j in 1 until w) best = maxOf(best, dp[h][j] + dp[h][w - j])
                dp[h][w] = best
            }
        }
        return dp[m][n]
    }
}
