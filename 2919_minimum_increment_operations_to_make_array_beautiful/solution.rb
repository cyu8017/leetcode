# LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_increment_operations(nums, k)
  dp0 = dp1 = dp2 = 0
  nums.each do |v|
    cost = v < k ? k - v : 0
    nd0 = cost + [dp0, dp1, dp2].min
    dp0, dp1, dp2 = dp1, dp2, nd0
  end
  [dp0, dp1, dp2].min
end
