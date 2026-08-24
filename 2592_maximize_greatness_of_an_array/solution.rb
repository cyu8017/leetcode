# LeetCode 2592 - Maximize Greatness of an Array
# https://leetcode.com/problems/maximize-greatness-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def maximize_greatness(nums)
  nums = nums.sort
  i = 0
  nums.each { |x| i += 1 if x > nums[i] }
  i
end
