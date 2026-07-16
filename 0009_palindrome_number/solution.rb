# LeetCode 0009 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  return false if x.negative? || (x != 0 && x % 10 == 0)

  reversed_half = 0
  while x > reversed_half
    reversed_half = reversed_half * 10 + x % 10
    x /= 10
  end

  x == reversed_half || x == reversed_half / 10
end
