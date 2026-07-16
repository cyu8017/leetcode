# LeetCode 0322 - Coin Change
# https://leetcode.com/problems/coin-change/

class Solution
  def coinChange(coins, amount)
    max_value = amount + 1
    dp = Array.new(amount + 1, max_value)
    dp[0] = 0
    coins.each do |coin|
      (coin..amount).each do |value|
        dp[value] = [dp[value], dp[value - coin] + 1].min
      end
    end
    dp[amount] == max_value ? -1 : dp[amount]
  end
end
