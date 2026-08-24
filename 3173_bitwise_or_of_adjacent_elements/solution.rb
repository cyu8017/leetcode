# LeetCode 3173 - Bitwise OR of Adjacent Elements
# https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

# @param {Integer[]} nums
# @return {Integer[]}
def or_array(nums)
  ans = Array.new(nums.length - 1, 0)
  (1...nums.length).each { |i| ans[i - 1] = nums[i] | nums[i - 1] }
  ans
end
