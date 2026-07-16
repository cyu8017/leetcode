# LeetCode 0121 - Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  minimum = Float::INFINITY
  profit = 0
  prices.each do |price|
    minimum = [minimum, price].min
    profit = [profit, price - minimum].max
  end
  profit
end