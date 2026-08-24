# LeetCode 3339 - Find the Number of K-Even Arrays
# https://leetcode.com/problems/find-the-number-of-k-even-arrays/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def count_of_arrays(n, m, k)
  mod = 1_000_000_007
  even = m / 2
  odd = m - even
  dp = Array.new(n + 1) { Array.new(k + 1) { [0, 0] } }
  dp[1][0][0] = odd
  dp[1][0][1] = even
  (1...n).each do |i|
    (0..k).each do |j|
      dp[i + 1][j][0] = (dp[i + 1][j][0] + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod) % mod
      dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod
      if j < k
        dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod) % mod
      end
    end
  end
  (dp[n][k][0] + dp[n][k][1]) % mod
end
