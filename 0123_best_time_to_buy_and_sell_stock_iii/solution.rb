# LeetCode 0123 - Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  buy_one = Float::INFINITY
  buy_two = Float::INFINITY
  sell_one = 0
  sell_two = 0

  prices.each do |price|
    buy_one = [buy_one, price].min
    sell_one = [sell_one, price - buy_one].max
    buy_two = [buy_two, price - sell_one].min
    sell_two = [sell_two, price - buy_two].max
  end
  sell_two
end