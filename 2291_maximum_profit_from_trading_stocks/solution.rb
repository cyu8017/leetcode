# LeetCode 2291 - Maximum Profit From Trading Stocks
# https://leetcode.com/problems/maximum-profit-from-trading-stocks/

# @param {Integer[]} present
# @param {Integer[]} future
# @param {Integer} budget
# @return {Integer}
def maximum_profit(present, future, budget)
  n = present.length
  dp = Array.new(budget + 1, 0)
  n.times do |i|
    profit = future[i] - present[i]
    next if profit <= 0

    cost = present[i]
    budget.downto(cost) do |b|
      dp[b] = [dp[b], dp[b - cost] + profit].max
    end
  end
  dp[budget]
end

alias solve maximum_profit
