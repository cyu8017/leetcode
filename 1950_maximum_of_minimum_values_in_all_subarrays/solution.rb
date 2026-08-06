# LeetCode 1950 - Maximum of Minimum Values in All Subarrays
# https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

# @param {Integer[]} nums
# @return {Integer[]}
def find_maximums(nums)
  n = nums.length
  left = Array.new(n, -1)
  right = Array.new(n, n)
  stack = []
  nums.each_with_index do |x, i|
    stack.pop while !stack.empty? && nums[stack[-1]] >= x
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end
  stack = []
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] >= nums[i]
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end
  ans = Array.new(n, 0)
  nums.each_with_index do |x, i|
    length = right[i] - left[i] - 1
    ans[length - 1] = [ans[length - 1], x].max
  end
  (n - 2).downto(0) { |i| ans[i] = [ans[i], ans[i + 1]].max }
  ans
end
