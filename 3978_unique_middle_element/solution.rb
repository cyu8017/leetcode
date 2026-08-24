# LeetCode 3978 - Unique Middle Element
# https://leetcode.com/problems/unique-middle-element/

# @param {Integer[]} nums
# @return {Boolean}
def is_middle_element_unique(nums)
  mid = nums[nums.length / 2]
  nums.count(mid) == 1
end
