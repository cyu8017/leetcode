# LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

# @param {Integer[]} nums
# @return {Integer}
def count_elements(nums)
  mn = nums.min
  mx = nums.max
  nums.count { |x| x > mn && x < mx }
end
