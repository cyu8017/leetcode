# LeetCode 0456 - 132 Pattern
# https://leetcode.com/problems/132-pattern/

class Solution
  def find132pattern(nums)
    stack = []
    third = -Float::INFINITY

    nums.reverse_each do |value|
      return true if value < third

      while !stack.empty? && value > stack.last
        third = stack.pop
      end
      stack << value
    end

    false
  end
end
