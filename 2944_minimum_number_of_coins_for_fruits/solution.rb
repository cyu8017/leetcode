# LeetCode 2944 - Minimum Number of Coins for Fruits
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

# @param {Integer[]} prices
# @return {Integer}
def minimum_coins(prices)
  n = prices.length
  dp = Array.new(n + 1, 1 << 30)
  dp[0] = 0
  (1..n).each do |i|
    j = i
    while j <= n && j <= i + i
      cand = dp[i - 1] + prices[i - 1]
      dp[j] = cand if cand < dp[j]
      j += 1
    end
  end
  dp[n]
end
