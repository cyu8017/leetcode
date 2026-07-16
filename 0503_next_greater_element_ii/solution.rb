# LeetCode 0503 - Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/

class Solution
  def next_greater_elements(nums)
    length = nums.length
    result = Array.new(length, -1)
    stack = []

    (length * 2).times do |index|
      while !stack.empty? && nums[stack[-1]] < nums[index % length]
        result[stack.pop] = nums[index % length]
      end
      stack << index if index < length
    end

    result
  end

  alias_method :nextGreaterElements, :next_greater_elements
end
