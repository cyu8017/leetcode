# LeetCode 3001 - Minimum Moves to Capture The Queen
# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @param {Integer} d
# @param {Integer} e
# @param {Integer} f
# @return {Integer}
def min_moves_to_capture_the_queen(a, b, c, d, e, f)
  return 1 if a == e && (c != a || (d - b) * (d - f) > 0)
  return 1 if b == f && (d != b || (c - a) * (c - e) > 0)
  return 1 if c - e == d - f && (a - e != b - f || (a - c) * (a - e) > 0)
  return 1 if c - e == f - d && (a - e != f - b || (a - c) * (a - e) > 0)

  2
end
