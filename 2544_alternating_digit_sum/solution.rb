# LeetCode 2544 - Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/

# @param {Integer} n
# @return {Integer}
def alternate_digit_sum(n)
  digits = []
  x = n
  while x > 0
    digits << (x % 10)
    x /= 10
  end
  ans = 0
  sign = 1
  (digits.length - 1).downto(0) do |i|
    ans += sign * digits[i]
    sign = -sign
  end
  ans
end
