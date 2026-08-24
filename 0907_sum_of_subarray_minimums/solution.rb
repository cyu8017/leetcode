# LeetCode 0907 - Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/

# @param {Integer[]} arr
# @return {Integer}
def sum_subarray_mins(arr)
  mod = 10**9 + 7
  n = arr.length
  left = Array.new(n, -1)
  right = Array.new(n, n)
  stack = []
  n.times do |i|
    stack.pop while !stack.empty? && arr[stack[-1]] > arr[i]
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end
  stack.clear
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && arr[stack[-1]] >= arr[i]
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end
  (0...n).sum { |i| arr[i] * (i - left[i]) * (right[i] - i) } % mod
end
