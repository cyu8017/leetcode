# LeetCode 1037 - Valid Boomerang
# https://leetcode.com/problems/valid-boomerang/

# @param {Integer[][]} points
# @return {Boolean}
def is_boomerang(points)
  x1, y1 = points[0]
  x2, y2 = points[1]
  x3, y3 = points[2]
  (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1)
end
