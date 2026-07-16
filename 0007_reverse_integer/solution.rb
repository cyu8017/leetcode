# LeetCode 0007 - Reverse Integer
# https://leetcode.com/problems/reverse-integer/

# @param {Integer} x
# @return {Integer}
def reverse(x)
  limit = 2**31 - 1
  result = 0
  negative = x.negative?
  x = x.abs

  while x.positive?
    result = result * 10 + x % 10
    x /= 10
  end

  return 0 if result > limit

  negative ? -result : result
end
