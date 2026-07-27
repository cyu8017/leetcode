# LeetCode 1610 - Maximum Number of Visible Points
# https://leetcode.com/problems/maximum-number-of-visible-points/

# @param {Integer[][]} points
# @param {Integer} angle
# @param {Integer[]} location
# @return {Integer}
def visible_points(points, angle, location)
  same = 0
  a = []
  points.each do |x, y|
    dx = x - location[0]
    dy = y - location[1]
    if dx.zero? && dy.zero?
      same += 1
    else
      a << Math.atan2(dy, dx)
    end
  end
  a.sort!
  ext = a + a.map { |x| x + 2 * Math::PI }
  width = angle * Math::PI / 180.0 + 1e-12
  left = 0
  best = 0
  ext.each_with_index do |value, right|
    left += 1 while value - ext[left] > width
    best = [best, [a.length, right - left + 1].min].max
  end
  best + same
end
