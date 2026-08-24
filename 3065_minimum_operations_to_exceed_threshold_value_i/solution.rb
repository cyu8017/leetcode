# LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  nums.count { |x| x < k }
end
