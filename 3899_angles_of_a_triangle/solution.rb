# LeetCode 3899 - Angles of a Triangle
# https://leetcode.com/problems/angles-of-a-triangle/

# @param {Float[]} sides
# @return {Float[]}
def internal_angles(sides)
  sides = sides.sort
  a, b, c = sides[0], sides[1], sides[2]
  return [] if a + b <= c
  pi = Math.acos(-1.0)
  aa = Math.acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / pi
  bb = Math.acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / pi
  cc = 180.0 - aa - bb
  [aa, bb, cc]
end
