# LeetCode 0414 - Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

class Solution
  def third_max(nums)
    first = second = third = nil

    nums.each do |value|
      next if value == first || value == second || value == third

      if first.nil? || value > first
        third, second, first = second, first, value
      elsif second.nil? || value > second
        third, second = second, value
      elsif third.nil? || value > third
        third = value
      end
    end

    third.nil? ? first : third
  end

  alias_method :thirdMax, :third_max
end
