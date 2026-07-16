# LeetCode 0376 - Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/

class Solution
  def wiggle_max_length(nums)
    return nums.length if nums.length < 2

    up = 1
    down = 1
    1.upto(nums.length - 1) do |index|
      if nums[index] > nums[index - 1]
        up = down + 1
      elsif nums[index] < nums[index - 1]
        down = up + 1
      end
    end

    [up, down].max
  end

  alias_method :wiggleMaxLength, :wiggle_max_length
end
