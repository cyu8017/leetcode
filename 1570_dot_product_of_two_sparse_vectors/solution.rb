# LeetCode 1570 - Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector
  attr_reader :values

  def initialize(nums)
    @values = {}
    nums.each_with_index { |x, i| @values[i] = x if x != 0 }
  end

  def dot_product(vec)
    return vec.dot_product(self) if @values.length > vec.values.length
    @values.sum { |i, x| x * (vec.values[i] || 0) }
  end
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def dot_product(nums1, nums2)
  SparseVector.new(nums1).dot_product(SparseVector.new(nums2))
end
