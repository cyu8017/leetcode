# LeetCode 1913 - Maximum Product Difference Between Two Pairs
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

# @param {Integer[]} nums
# @return {Integer}
def max_product_difference(nums)
  a = b = 0
  c = d = 100_000
  nums.each do |x|
    if x > a
      b = a
      a = x
    elsif x > b
      b = x
    end
    if x < c
      d = c
      c = x
    elsif x < d
      d = x
    end
  end
  a * b - c * d
end
