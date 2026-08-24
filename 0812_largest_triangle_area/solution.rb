# LeetCode 0812 - Largest Triangle Area
# https://leetcode.com/problems/largest-triangle-area/

# @param {Integer[][]} points
# @return {Float}
def largest_triangle_area(points)
  best = 0.0
  n = points.length
  n.times do |i|
    x1, y1 = points[i]
    ((i + 1)...n).each do |j|
      x2, y2 = points[j]
      ((j + 1)...n).each do |k|
        x3, y3 = points[k]
        area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)).abs / 2.0
        best = area if area > best
      end
    end
  end
  best
end
