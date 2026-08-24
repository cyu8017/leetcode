# LeetCode 3674 - Minimum Operations to Equalize Array
# https://leetcode.com/problems/minimum-operations-to-equalize-array/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  nums.each { |x| return 1 if x != nums[0] }
  0
end
