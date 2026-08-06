# LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def num_triplets(nums1, nums2)
  count = lambda do |a, b|
    squares = Hash.new(0)
    a.each { |x| squares[x * x] += 1 }
    products = Hash.new(0)
    b.each_with_index do |bi, i|
      ((i + 1)...b.length).each { |j| products[bi * b[j]] += 1 }
    end
    squares.sum { |value, cnt| cnt * (products[value] || 0) }
  end
  count.call(nums1, nums2) + count.call(nums2, nums1)
end
