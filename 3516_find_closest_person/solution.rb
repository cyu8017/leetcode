# LeetCode 3516 - Find Closest Person
# https://leetcode.com/problems/find-closest-person/

# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def find_closest(x, y, z)
  a = (x - z).abs
  b = (y - z).abs
  return 0 if a == b
  a < b ? 1 : 2
end
