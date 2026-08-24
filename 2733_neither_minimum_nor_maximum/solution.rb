# LeetCode 2733 - Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/

# @param {Integer[]} nums
# @return {Integer}
def find_non_min_or_max(nums)
  return -1 if nums.length < 3
  a, b, c = nums[0], nums[1], nums[2]
  a + b + c - [a, b, c].max - [a, b, c].min
end
