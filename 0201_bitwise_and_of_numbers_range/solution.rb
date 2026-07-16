# LeetCode 0201 - Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/

# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def range_bitwise_and(left, right)
  shift = 0
  while left < right
    left >>= 1
    right >>= 1
    shift += 1
  end
  left << shift
end