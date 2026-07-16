# LeetCode 0518 - Coin Change II
# https://leetcode.com/problems/coin-change-ii/

class Solution
  def change(amount, coins)
    dp = Array.new(amount + 1, 0)
    dp[0] = 1

    coins.each do |coin|
      (coin..amount).each do |value|
        dp[value] += dp[value - coin]
      end
    end

    dp[amount]
  end
end
