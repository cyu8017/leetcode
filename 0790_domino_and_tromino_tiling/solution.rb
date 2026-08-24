# LeetCode 0790 - Domino and Tromino Tiling
# https://leetcode.com/problems/domino-and-tromino-tiling/

# @param {Integer} n
# @return {Integer}
def num_tilings(n)
  mod = 10**9 + 7
  return 1 if n == 1
  return 2 if n == 2

  dp = Array.new(n + 1, 0)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 5
  (4..n).each { |i| dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod }
  dp[n]
end
