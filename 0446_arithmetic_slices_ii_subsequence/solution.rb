# LeetCode 0446 - Arithmetic Slices II - Subsequence
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution
  def number_of_arithmetic_slices(nums)
    total = 0
    differences = Array.new(nums.length) { Hash.new(0) }

    nums.each_with_index do |value, index|
      (0...index).each do |previous|
        diff = value - nums[previous]
        total += differences[previous][diff]
        differences[index][diff] += differences[previous][diff] + 1
      end
    end

    total
  end

  alias_method :numberOfArithmeticSlices, :number_of_arithmetic_slices
end
