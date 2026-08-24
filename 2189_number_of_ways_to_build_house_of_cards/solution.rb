# LeetCode 2189 - Number of Ways to Build House of Cards
# https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

# @param {Integer} n
# @return {Integer}
def house_of_cards(n)
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  k = 1
  while 3 * k - 1 <= n
    cost = 3 * k - 1
    n.downto(cost) { |j| dp[j] += dp[j - cost] }
    k += 1
  end
  dp[n]
end
