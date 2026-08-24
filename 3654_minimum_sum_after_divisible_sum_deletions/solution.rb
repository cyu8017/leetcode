# LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
# https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_array_sum(nums, k)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = (prefix[i] + nums[i]) % k }
  inf = 10**18
  dp = Array.new(n + 1, 0)
  best = Array.new(k, inf)
  best[0] = 0
  (1..n).each do |i|
    dp[i] = dp[i - 1] + nums[i - 1]
    dp[i] = best[prefix[i]] if best[prefix[i]] < dp[i]
    best[prefix[i]] = dp[i] if dp[i] < best[prefix[i]]
  end
  dp[n]
end
