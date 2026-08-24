# LeetCode 3798 - Largest Even Number
# https://leetcode.com/problems/largest-even-number/

# @param {String} s
# @return {String}
def largest_even(s)
  s = s[0...-1] while s.length > 0 && s[-1] == "1"
  s
end
