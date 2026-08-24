# LeetCode 3667 - Sort Array By Absolute Value
# https://leetcode.com/problems/sort-array-by-absolute-value/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_by_absolute_value(nums)
  nums.sort_by(&:abs)
end
