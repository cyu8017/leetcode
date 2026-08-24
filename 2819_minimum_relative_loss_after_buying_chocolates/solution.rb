# LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
# https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

# @param {Integer[]} prices
# @param {Integer[][]} queries
# @return {Integer[]}
def minimum_relative_losses(prices, queries)
  prices = prices.sort
  n = prices.length
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(kk, m), qi|
    losses = Array.new(n, 0)
    (0...n).each do |i|
      losses[i] = prices[i] <= kk ? prices[i] : 2 * kk - prices[i]
    end
    losses.sort!
    total = 0
    (0...m).each { |i| total += losses[i] }
    ans[qi] = total
  end
  ans
end
