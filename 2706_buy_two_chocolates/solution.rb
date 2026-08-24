# LeetCode 2706 - Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/

# @param {Integer[]} prices
# @param {Integer} money
# @return {Integer}
def buy_choco(prices, money)
  prices = prices.sort
  cost = prices[0] + prices[1]
  cost <= money ? money - cost : money
end
