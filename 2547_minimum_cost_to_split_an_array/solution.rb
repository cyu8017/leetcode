# LeetCode 2547 - Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_cost(nums, k)
  n = nums.length
  inf = 10**18
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  n.times do |i|
    freq = Hash.new(0)
    trimmed = 0
    (i...n).each do |j|
      c = freq[nums[j]] + 1
      freq[nums[j]] = c
      if c == 2
        trimmed += 2
      elsif c > 2
        trimmed += 1
      end
      cost = dp[i] + k + trimmed
      dp[j + 1] = cost if cost < dp[j + 1]
    end
  end
  dp[n]
end
