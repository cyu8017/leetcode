# LeetCode 2830 - Maximize the Profit as the Salesman
# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

# @param {Integer} n
# @param {Integer[][]} offers
# @return {Integer}
def maximize_the_profit(n, offers)
  by_end = Array.new(n) { [] }
  offers.each { |o| by_end[o[1]] << o }
  dp = Array.new(n + 1, 0)
  (0...n).each do |en|
    dp[en + 1] = dp[en]
    by_end[en].each { |o| dp[en + 1] = [dp[en + 1], dp[o[0]] + o[2]].max }
  end
  dp[n]
end
