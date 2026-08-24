# LeetCode 0962 - Maximum Width Ramp
# https://leetcode.com/problems/maximum-width-ramp/

# @param {Integer[]} nums
# @return {Integer}
def max_width_ramp(nums)
  stack = []
  nums.each_with_index do |x, i|
    stack << i if stack.empty? || nums[stack[-1]] > x
  end
  ans = 0
  (nums.length - 1).downto(0) do |j|
    while !stack.empty? && nums[stack[-1]] <= nums[j]
      ans = [ans, j - stack.pop].max
    end
  end
  ans
end
