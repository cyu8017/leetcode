# LeetCode 1692 - Count Ways to Distribute Candies
# https://leetcode.com/problems/count-ways-to-distribute-candies/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def ways_to_distribute(n, k)
  mod = 10**9 + 7
  dp = Array.new(k + 1, 0)
  dp[0] = 1
  (1..n).each do |i|
    [i, k].min.downto(1) do |j|
      dp[j] = (dp[j - 1] + j * dp[j]) % mod
    end
    dp[0] = 0
  end
  dp[k]
end
