# LeetCode 1134 - Armstrong Number
# https://leetcode.com/problems/armstrong-number/

# @param {Integer} n
# @return {Boolean}
def is_armstrong(n)
  digits = n.to_s
  power = digits.length
  n == digits.chars.sum { |d| d.to_i**power }
end
