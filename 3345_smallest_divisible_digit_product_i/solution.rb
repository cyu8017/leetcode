# LeetCode 3345 - Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/

# @param {Integer} n
# @param {Integer} t
# @return {Integer}
def smallest_number(n, t)
  x = n
  loop do
    p = 1
    y = x
    while y > 0
      p *= y % 10
      y /= 10
    end
    return x if p % t == 0

    x += 1
  end
end
