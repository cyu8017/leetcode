// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

class Solution {
    fun numMusicPlaylists(n: Int, goal: Int, k: Int): Int {
        var MOD = 1_000_000_007
        var dp = Array(goal + 1) { LongArray(n + 1) }
        dp[0][0] = 1
        for (i in 1 until = goal) {
            for (j in 1 until = i && j <= n) {
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD
                if (j > k) dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
            }
        }
        return dp[goal][n]
    }
}
