# LeetCode 0334 - Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution
  def increasing_triplet(nums)
    first = second = Float::INFINITY
    nums.each do |num|
      if num <= first
        first = num
      elsif num <= second
        second = num
      else
        return true
      end
    end
    false
  end

  alias_method :increasingTriplet, :increasing_triplet
end
