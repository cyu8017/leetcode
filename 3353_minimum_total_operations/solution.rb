# LeetCode 3353 - Minimum Total Operations
# https://leetcode.com/problems/minimum-total-operations/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  ops = 0
  (nums.length - 2).downto(0) { |i| ops += 1 if nums[i] != nums[i + 1] }
  ops
end
