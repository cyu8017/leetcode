// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution {
    fun minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int {
        val n = floor.length
        val dp = Array(numCarpets + 1) { IntArray(n + 1) { 1 shl 30 } }
        dp[0][0] = 0
        for (j in 1..n) {
            dp[0][j] = dp[0][j - 1] + if (floor[j - 1] == '1') 1 else 0
        }
        for (c in 1..numCarpets) {
            dp[c][0] = 0
            for (j in 1..n) {
                dp[c][j] = dp[c][j - 1] + if (floor[j - 1] == '1') 1 else 0
                val start = maxOf(0, j - carpetLen)
                dp[c][j] = minOf(dp[c][j], dp[c - 1][start])
            }
        }
        return dp[numCarpets][n]
    }
}
