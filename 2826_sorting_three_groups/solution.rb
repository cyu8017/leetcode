# LeetCode 2826 - Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  n = nums.length
  inf = 10**9
  dp = Array.new(n + 1) { Array.new(4, inf) }
  dp[0][1] = dp[0][2] = dp[0][3] = 0
  (1..n).each do |i|
    v = nums[i - 1]
    (1..3).each do |g|
      cost = v == g ? 0 : 1
      (1..g).each { |prev| dp[i][g] = [dp[i][g], dp[i - 1][prev] + cost].min }
    end
  end
  [dp[n][1], dp[n][2], dp[n][3]].min
end
