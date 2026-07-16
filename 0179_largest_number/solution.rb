# LeetCode 0179 - Largest Number
# https://leetcode.com/problems/largest-number/

class Solution
  def largest_number(nums)
    parts = nums.map(&:to_s).sort { |left, right| right + left <=> left + right }
    parts[0] == "0" ? "0" : parts.join
  end
end