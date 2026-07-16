# LeetCode 0089 - Gray Code
# https://leetcode.com/problems/gray-code/

# @param {Integer} n
# @return {Integer[]}
def gray_code(n)
  size = 1 << n
  (0...size).map { |i| i ^ (i >> 1) }
end
