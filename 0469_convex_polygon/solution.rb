# LeetCode 0469 - Convex Polygon
# https://leetcode.com/problems/convex-polygon/

class Solution
  def is_convex(points)
    direction = 0
    count = points.length

    count.times do |index|
      x1 = points[(index + 1) % count][0] - points[index][0]
      y1 = points[(index + 1) % count][1] - points[index][1]
      x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0]
      y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1]
      cross = x1 * y2 - y1 * x2
      next if cross.zero?

      current = cross.positive? ? 1 : -1
      return false if direction != 0 && direction != current

      direction = current if direction.zero?
    end

    true
  end

  alias_method :isConvex, :is_convex
end
