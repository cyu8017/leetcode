# LeetCode 0920 - Number of Music Playlists
# https://leetcode.com/problems/number-of-music-playlists/

# @param {Integer} n
# @param {Integer} goal
# @param {Integer} k
# @return {Integer}
def num_music_playlists(n, goal, k)
  mod = 10**9 + 7
  dp = Array.new(goal + 1) { Array.new(n + 1, 0) }
  dp[0][0] = 1
  (1..goal).each do |i|
    (1..[i, n].min).each do |j|
      dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % mod
      dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod if j > k
    end
  end
  dp[goal][n]
end
