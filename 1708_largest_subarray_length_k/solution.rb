# LeetCode 1708 - Largest Subarray Length K
# https://leetcode.com/problems/largest-subarray-length-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def largest_subarray(nums, k)
  start = (0..nums.length - k).max_by { |i| nums[i] }
  nums[start, k]
end
