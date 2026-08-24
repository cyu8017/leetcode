# LeetCode 3024 - Type of Triangle
# https://leetcode.com/problems/type-of-triangle/

# @param {Integer[]} nums
# @return {String}
def triangle_type(nums)
  nums = nums.sort
  return "none" if nums[0] + nums[1] <= nums[2]
  return "equilateral" if nums[0] == nums[2]
  return "isosceles" if nums[0] == nums[1] || nums[1] == nums[2]

  "scalene"
end
