# LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

# @param {Integer[]} prices
# @param {Integer[]} strategy
# @param {Integer} k
# @return {Integer}
def max_profit(prices, strategy, k)
  n = prices.length
  s = Array.new(n + 1, 0)
  t = Array.new(n + 1, 0)
  (1..n).each do |i|
    s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1]
    t[i] = t[i - 1] + prices[i - 1]
  end
  ans = s[n]
  (k..n).each do |i|
    v = s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2])
    ans = v if v > ans
  end
  ans
end
