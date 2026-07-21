# LeetCode 1865 - Finding Pairs With a Certain Sum
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs
  # @param {Integer[]} nums1
  # @param {Integer[]} nums2
  def initialize(nums1, nums2)
    @nums1 = nums1
    @nums2 = nums2
    @counts = Hash.new(0)
    nums2.each { |num| @counts[num] += 1 }
  end

  # @param {Integer} index
  # @param {Integer} val
  # @return {Void}
  def add(index, val)
    @counts[@nums2[index]] -= 1
    @nums2[index] += val
    @counts[@nums2[index]] += 1
    nil
  end

  # @param {Integer} tot
  # @return {Integer}
  def count(tot)
    @nums1.sum { |num| @counts[tot - num] }
  end
end
