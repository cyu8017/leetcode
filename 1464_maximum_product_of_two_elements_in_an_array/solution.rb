# LeetCode 1464 - Maximum Product Of Two Elements In An Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

def max_product(nums)
  a, b = nums.sort[-2..]
  (a - 1) * (b - 1)
end
