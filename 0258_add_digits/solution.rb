# LeetCode 0258 - Add Digits
# https://leetcode.com/problems/add-digits/

# @param {Integer} num
# @return {Integer}
def add_digits(num)
  return 0 if num.zero?

  1 + (num - 1) % 9
end
