# LeetCode 0303 - Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray
  def initialize(nums)
    @prefix = [0]
    nums.each { |num| @prefix << @prefix[-1] + num }
  end

  def sumRange(left, right)
    @prefix[right + 1] - @prefix[left]
  end
end
