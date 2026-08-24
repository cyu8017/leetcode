# LeetCode 0879 - Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/

# @param {Integer} n
# @param {Integer} min_profit
# @param {Integer[]} group
# @param {Integer[]} profit
# @return {Integer}
def profitable_schemes(n, min_profit, group, profit)
  mod = 10**9 + 7
  dp = Array.new(n + 1) { Array.new(min_profit + 1, 0) }
  dp[0][0] = 1
  group.zip(profit).each do |members, p|
    n.downto(members) do |people|
      min_profit.downto(0) do |prof|
        np = [min_profit, prof + p].min
        dp[people][np] = (dp[people][np] + dp[people - members][prof]) % mod
      end
    end
  end
  (0..n).sum { |people| dp[people][min_profit] } % mod
end
