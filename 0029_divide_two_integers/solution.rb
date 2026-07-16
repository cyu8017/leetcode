# LeetCode 0029 - Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

# @param {Integer} dividend
# @param {Integer} divisor
# @return {Integer}
def divide(dividend, divisor)
  return 2**31 - 1 if dividend == -2**31 && divisor == -1

  negative = (dividend < 0) ^ (divisor < 0)
  dividend = dividend.abs
  divisor = divisor.abs
  quotient = 0

  31.downto(0) do |i|
    if (dividend >> i) >= divisor
      quotient += 1 << i
      dividend -= divisor << i
    end
  end

  negative ? -quotient : quotient
end
