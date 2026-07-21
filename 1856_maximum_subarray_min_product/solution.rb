# LeetCode 1856 - Maximum Subarray Min-Product
# https://leetcode.com/problems/maximum-subarray-min-product/

# @param {Integer[]} nums
# @return {Integer}
def max_sum_min_product(nums)
  mod = 10**9 + 7
  n = nums.length
  prefix = Array.new(n + 1, 0)
  nums.each_with_index { |value, index| prefix[index + 1] = prefix[index] + value }

  left_bound = Array.new(n, -1)
  stack = []
  nums.each_with_index do |value, index|
    stack.pop while !stack.empty? && nums[stack[-1]] >= value
    left_bound[index] = stack.empty? ? -1 : stack[-1]
    stack << index
  end

  right_bound = Array.new(n, n)
  stack.clear
  (n - 1).downto(0) do |index|
    value = nums[index]
    stack.pop while !stack.empty? && nums[stack[-1]] >= value
    right_bound[index] = stack.empty? ? n : stack[-1]
    stack << index
  end

  best = 0
  nums.each_with_index do |value, index|
    total = prefix[right_bound[index]] - prefix[left_bound[index] + 1]
    best = [best, total * value].max
  end

  best % mod
end
