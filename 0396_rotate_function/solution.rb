# LeetCode 0396 - Rotate Function
# https://leetcode.com/problems/rotate-function/

class Solution
  def max_rotate_function(nums)
    total = nums.sum
    current = nums.each_with_index.sum { |value, index| index * value }
    best = current

    (nums.length - 1).downto(1) do |index|
      current += total - nums.length * nums[index]
      best = [best, current].max
    end

    best
  end

  alias_method :maxRotateFunction, :max_rotate_function
end
