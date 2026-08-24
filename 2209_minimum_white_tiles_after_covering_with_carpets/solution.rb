# LeetCode 2209 - Minimum White Tiles After Covering With Carpets
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

# @param {String} floor
# @param {Integer} num_carpets
# @param {Integer} carpet_len
# @return {Integer}
def minimum_white_tiles(floor, num_carpets, carpet_len)
  n = floor.length
  inf = 1 << 30
  dp = Array.new(num_carpets + 1) { Array.new(n + 1, inf) }
  dp[0][0] = 0
  (1..n).each do |j|
    dp[0][j] = dp[0][j - 1] + (floor[j - 1] == "1" ? 1 : 0)
  end
  (1..num_carpets).each do |c|
    dp[c][0] = 0
    (1..n).each do |j|
      dp[c][j] = dp[c][j - 1] + (floor[j - 1] == "1" ? 1 : 0)
      start = [0, j - carpet_len].max
      dp[c][j] = [dp[c][j], dp[c - 1][start]].min
    end
  end
  dp[num_carpets][n]
end
