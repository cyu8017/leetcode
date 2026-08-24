# LeetCode 3908 - Valid Digit Number
# https://leetcode.com/problems/valid-digit-number/

# @param {Integer} n
# @param {Integer} x
# @return {Boolean}
def valid_digit(n, x)
  has_x = false
  while n > 9
    has_x ||= n % 10 == x
    n /= 10
  end
  has_x && n != x
end
