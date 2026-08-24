# LeetCode 2695 - Array Wrapper
# https://leetcode.com/problems/array-wrapper/

class ArrayWrapper
  def initialize(nums)
    @nums = nums
  end

  def value_of
    s = 0
    @nums.each { |x| s += x }
    s
  end

  def +(other)
    value_of + other.value_of
  end

  def to_i
    value_of
  end

  def to_s
    "[" + @nums.map(&:to_s).join(",") + "]"
  end
end

# @param {Integer[]} nums
# @return {ArrayWrapper}
def array_wrapper(nums)
  ArrayWrapper.new(nums)
end
