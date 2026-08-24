# LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def valid_subarray_size(nums, threshold)
  n = nums.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  stack = []
  (0...n).each do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] >= nums[i]
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end
  stack.clear
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] >= nums[i]
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end
  best = -1
  (0...n).each do |i|
    k = right[i] - left[i] - 1
    next unless nums[i] > threshold / k
    best = k if best == -1 || k < best
  end
  best
end
