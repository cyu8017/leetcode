# LeetCode 3099 - Harshad Number
# https://leetcode.com/problems/harshad-number/

# @param {Integer} x
# @return {Integer}
def sum_of_the_digits_of_harshad_number(x)
  s = 0
  y = x
  while y > 0
    s += y % 10
    y /= 10
  end
  x % s == 0 ? s : -1
end
