# LeetCode 1874 - Minimize Product Sum of Two Arrays
# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_product_sum(nums1, nums2)
  nums1 = nums1.sort
  nums2 = nums2.sort.reverse
  nums1.zip(nums2).sum { |a, b| a * b }
end
