# LeetCode 3689 - Maximum Total Subarray Value I
# https://leetcode.com/problems/maximum-total-subarray-value-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_total_value(nums, k)
  k * (nums.max - nums.min)
end
