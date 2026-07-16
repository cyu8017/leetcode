# LeetCode 0163 - Missing Ranges
# https://leetcode.com/problems/missing-ranges/

class Solution
  def find_missing_ranges(nums, lower, upper)
    result = []
    previous = lower - 1
    (nums + [upper + 1]).each do |number|
      result << [previous + 1, number - 1] if number - previous >= 2
      previous = number
    end
    result
  end
end