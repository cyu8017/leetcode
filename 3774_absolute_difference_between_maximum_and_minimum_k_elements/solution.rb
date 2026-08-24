# LeetCode 3774 - Absolute Difference Between Maximum and Minimum K Elements
# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def abs_difference(nums, k)
  a = nums.sort
  ans = 0
  n = a.length
  (0...k).each { |i| ans += a[n - i - 1] - a[i] }
  ans
end
