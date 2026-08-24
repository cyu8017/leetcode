# LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

# @param {Integer[]} prices
# @param {Integer[]} profits
# @return {Integer}
def max_profit(prices, profits)
  n = prices.length
  ans = -1
  (0...n).each do |j|
    best_l = -1
    best_r = -1
    (0...j).each do |i|
      best_l = profits[i] if prices[i] < prices[j] && profits[i] > best_l
    end
    (j + 1...n).each do |k|
      best_r = profits[k] if prices[k] > prices[j] && profits[k] > best_r
    end
    if best_l >= 0 && best_r >= 0
      cand = best_l + profits[j] + best_r
      ans = cand if cand > ans
    end
  end
  ans
end
