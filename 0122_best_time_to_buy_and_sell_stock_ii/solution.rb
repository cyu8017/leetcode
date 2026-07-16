# LeetCode 0122 - Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  prices.each_cons(2).sum { |previous, current| [current - previous, 0].max }
end