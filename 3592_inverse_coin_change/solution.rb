# LeetCode 3592 - Inverse Coin Change
# https://leetcode.com/problems/inverse-coin-change/

# @param {Integer[]} num_ways
# @return {Integer[]}
def find_coins(num_ways)
  n = num_ways.length
  dp = Array.new(n + 1, 0)
  coins = []
  dp[0] = 1
  (1..n).each do |amt|
    ways = num_ways[amt - 1]
    next if dp[amt] == ways
    if dp[amt] + 1 == ways
      coins << amt
      (amt..n).each { |x| dp[x] += dp[x - amt] }
      return [] if dp[amt] != ways
      next
    end
    return []
  end
  coins
end
