# LeetCode 0384 - Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/

class Solution
  def initialize(nums)
    @original = nums.dup
    srand(47)
  end

  def reset
    @original.dup
  end

  def shuffle
    result = @original.dup
    result.shuffle!
    result
  end
end
