# LeetCode 2864 - Maximum Odd Binary Number
# https://leetcode.com/problems/maximum-odd-binary-number/

# @param {String} s
# @return {String}
def maximum_odd_binary_number(s)
  ones = s.count("1")
  zeros = s.length - ones
  "1" * (ones - 1) + "0" * zeros + "1"
end
