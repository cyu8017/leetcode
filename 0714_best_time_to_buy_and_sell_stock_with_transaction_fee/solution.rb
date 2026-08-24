# LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# @param {Integer[]} prices
# @param {Integer} fee
# @return {Integer}
def max_profit(prices, fee)
  hold = -prices[0]
  cash = 0
  prices[1..].each do |price|
    hold = [hold, cash - price].max
    cash = [cash, hold + price - fee].max
  end
  cash
end
