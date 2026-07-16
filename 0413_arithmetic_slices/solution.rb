# LeetCode 0413 - Arithmetic Slices
# https://leetcode.com/problems/arithmetic-slices/

class Solution
  def number_of_arithmetic_slices(nums)
    return 0 if nums.length < 3

    total = 0
    current = 0
    (2...nums.length).each do |index|
      if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]
        current += 1
        total += current
      else
        current = 0
      end
    end
    total
  end

  alias_method :numberOfArithmeticSlices, :number_of_arithmetic_slices
end
