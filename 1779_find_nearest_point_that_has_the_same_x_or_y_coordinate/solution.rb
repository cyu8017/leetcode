# LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

# @param {Integer} x
# @param {Integer} y
# @param {Integer[][]} points
# @return {Integer}
def nearest_valid_point(x, y, points)
  best = Float::INFINITY
  ans = -1
  points.each_with_index do |(px, py), i|
    next if px != x && py != y
    dist = (px - x).abs + (py - y).abs
    if dist < best
      best = dist
      ans = i
    end
  end
  ans
end
