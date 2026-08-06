# LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def is_majority_element(nums, target)
  left = nums.bsearch_index { |x| x >= target } || nums.length
  right = nums.bsearch_index { |x| x > target } || nums.length
  right - left > nums.length / 2
end
