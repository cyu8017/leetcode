# LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# @param {Integer} n
# @return {Integer}
def subtract_product_and_sum(n)
  product = 1
  total = 0
  while n > 0
    n, digit = n.divmod(10)
    product *= digit
    total += digit
  end
  product - total
end
