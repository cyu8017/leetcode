# LeetCode 2454 - Next Greater Element IV
# https://leetcode.com/problems/next-greater-element-iv/

# @param {Integer[]} nums
# @return {Integer[]}
def second_greater_element(nums)
  n = nums.length
  ans = Array.new(n, -1)
  stack1 = []
  stack2 = []
  (0...n).each do |i|
    x = nums[i]
    ans[stack2.pop] = x while !stack2.empty? && nums[stack2[-1]] < x
    tmp = []
    tmp << stack1.pop while !stack1.empty? && nums[stack1[-1]] < x
    (tmp.length - 1).downto(0) { |j| stack2 << tmp[j] }
    stack1 << i
  end
  ans
end
