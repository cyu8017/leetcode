# LeetCode 3536 - Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/

# @param {Integer} n
# @return {Integer}
def max_product(n)
  a = 0
  b = 0
  while n > 0
    x = n % 10
    n /= 10
    if a < x
      b = a
      a = x
    elsif b < x
      b = x
    end
  end
  a * b
end
