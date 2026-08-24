# LeetCode 3676 - Count Bowl Subarrays
# https://leetcode.com/problems/count-bowl-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def bowl_subarrays(nums)
  n = nums.length
  ans = 0
  ngr = Array.new(n, -1)
  ngl = Array.new(n, -1)
  stack = []
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] < nums[i]
    ngr[i] = stack[-1] unless stack.empty?
    stack << i
  end
  stack.clear
  (0...n).each do |i|
    stack.pop while !stack.empty? && nums[stack[-1]] < nums[i]
    ngl[i] = stack[-1] unless stack.empty?
    stack << i
  end
  (0...n).each do |i|
    ans += 1 if ngr[i] != -1 && ngr[i] - i >= 2
    ans += 1 if ngl[i] != -1 && i - ngl[i] >= 2
  end
  ans
end
