# LeetCode 2289 - Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/

# @param {Integer[]} nums
# @return {Integer}
def total_steps(nums)
  stack = []
  ans = 0
  (nums.length - 1).downto(0) do |i|
    steps = 0
    while !stack.empty? && nums[i] > stack[-1][0]
      steps = [steps, stack[-1][1]].max
      stack.pop
      steps += 1
    end
    ans = [ans, steps].max
    stack << [nums[i], steps]
  end
  ans
end
