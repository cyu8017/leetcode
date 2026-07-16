# LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution
  def maxProfit(prices)
    return 0 if prices.empty?

    free = 0
    hold = -prices[0]
    cooldown = 0
    prices[1..].each do |price|
      next_free = [free, cooldown].max
      next_hold = [hold, free - price].max
      next_cooldown = hold + price
      free = next_free
      hold = next_hold
      cooldown = next_cooldown
    end
    [free, cooldown].max
  end
end
