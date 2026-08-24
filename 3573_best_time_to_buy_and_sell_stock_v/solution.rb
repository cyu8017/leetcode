# LeetCode 3573 - Best Time to Buy and Sell Stock V
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

# @param {Integer[]} prices
# @param {Integer} k
# @return {Integer}
def maximum_profit(prices, k)
  n = prices.length
  f = Array.new(n) { Array.new(k + 1) { [0, 0, 0] } }
  (1..k).each do |j|
    f[0][j][1] = -prices[0]
    f[0][j][2] = prices[0]
  end
  (1...n).each do |i|
    (1..k).each do |j|
      f[i][j][0] = [f[i - 1][j][0], [f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]].max].max
      f[i][j][1] = [f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]].max
      f[i][j][2] = [f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]].max
    end
  end
  f[n - 1][k][0]
end
