# LeetCode 3993 - Maximum Value of an Alternating Sequence
# https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

# @param {Integer} n
# @param {Integer} s
# @param {Integer} m
# @return {Integer}
def maximum_value(n, s, m)
  return s if n == 1
  s + (n / 2) * (m - 1) + 1
end
