// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

object Solution {
  def numMusicPlaylists(n: Int, goal: Int, k: Int): Int = {
    val MOD = 1000000007
    val dp = Array.ofDim[Long](goal + 1, n + 1)
    dp(0)(0) = 1
    var i = 1
    while (i <= goal) {
      var j = 1
      while (j <= i && j <= n) {
        dp(i)(j) = dp(i - 1)(j - 1) * (n - j + 1) % MOD
        if (j > k) dp(i)(j) = (dp(i)(j) + dp(i - 1)(j) * (j - k)) % MOD
        j += 1
      }
      i += 1
    }
    dp(goal)(n).toInt
  }
}
