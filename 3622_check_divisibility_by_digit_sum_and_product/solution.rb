# LeetCode 3622 - Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

# @param {Integer} n
# @return {Boolean}
def check_divisibility(n)
  s = 0
  p = 1
  x = n
  while x != 0
    v = x % 10
    x /= 10
    s += v
    p *= v
  end
  n % (s + p) == 0
end
