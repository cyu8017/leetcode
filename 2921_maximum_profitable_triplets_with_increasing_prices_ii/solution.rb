# LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

# @param {Integer[]} prices
# @param {Integer[]} profits
# @return {Integer}
def max_profit(prices, profits)
  n = prices.length
  ans = -1
  bit = Array.new(5002, 0)

  update = lambda do |i, val|
    while i < bit.length
      bit[i] = val if val > bit[i]
      i += i & -i
    end
  end

  query = lambda do |i|
    best = -1
    while i > 0
      best = bit[i] if bit[i] > best
      i -= i & -i
    end
    best
  end

  max_left = Array.new(n, 0)
  (0...n).each do |j|
    max_left[j] = query.call(prices[j] - 1)
    update.call(prices[j], profits[j])
  end
  (0...n).each do |j|
    best_r = -1
    (j + 1...n).each do |k|
      best_r = profits[k] if prices[k] > prices[j] && profits[k] > best_r
    end
    if max_left[j] >= 0 && best_r >= 0
      cand = max_left[j] + profits[j] + best_r
      ans = cand if cand > ans
    end
  end
  ans
end
