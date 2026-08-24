# LeetCode 2518 - Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_partitions(nums, k)
  mod = 1_000_000_007
  total = nums.sum
  return 0 if total < 2 * k

  dp = Array.new(k, 0)
  dp[0] = 1
  nums.each do |x|
    (k - 1).downto(x) { |s| dp[s] = (dp[s] + dp[s - x]) % mod }
  end
  bad = 0
  dp.each { |v| bad = (bad + v) % mod }
  all_ways = 1
  nums.length.times { all_ways = all_ways * 2 % mod }
  (all_ways - 2 * bad % mod + mod) % mod
end
