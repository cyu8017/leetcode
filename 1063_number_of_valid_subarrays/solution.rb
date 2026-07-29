# LeetCode 1063 - Number of Valid Subarrays
# https://leetcode.com/problems/number-of-valid-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def valid_subarrays(nums)
  stack = []
  ans = 0
  nums.each_with_index do |x, i|
    while !stack.empty? && nums[stack[-1]] > x
      j = stack.pop
      ans += i - j
    end
    stack << i
  end
  while !stack.empty?
    j = stack.pop
    ans += nums.length - j
  end
  ans
end
