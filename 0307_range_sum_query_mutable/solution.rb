# LeetCode 0307 - Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/

class NumArray
  def initialize(nums)
    @nums = nums.dup
    @size = nums.length
    @tree = Array.new(@size + 1, 0)
    nums.each_with_index { |value, index| add(index + 1, value) }
  end

  def update(index, val)
    delta = val - @nums[index]
    @nums[index] = val
    add(index + 1, delta)
  end

  def sumRange(left, right)
    prefix(right + 1) - prefix(left)
  end

  private

  def add(index, delta)
    while index <= @size
      @tree[index] += delta
      index += index & -index
    end
  end

  def prefix(index)
    total = 0
    while index.positive?
      total += @tree[index]
      index -= index & -index
    end
    total
  end
end
