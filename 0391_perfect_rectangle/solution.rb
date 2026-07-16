# LeetCode 0391 - Perfect Rectangle
# https://leetcode.com/problems/perfect-rectangle/

require "set"

class Solution
  def is_rectangle_cover(rectangles)
    points = Set.new
    area = 0
    min_x = Float::INFINITY
    min_y = Float::INFINITY
    max_x = -Float::INFINITY
    max_y = -Float::INFINITY

    rectangles.each do |x1, y1, x2, y2|
      area += (x2 - x1) * (y2 - y1)
      min_x = [min_x, x1].min
      min_y = [min_y, y1].min
      max_x = [max_x, x2].max
      max_y = [max_y, y2].max

      [[x1, y1], [x1, y2], [x2, y1], [x2, y2]].each do |point|
        if points.include?(point)
          points.delete(point)
        else
          points.add(point)
        end
      end
    end

    corners = Set[[min_x, min_y], [min_x, max_y], [max_x, min_y], [max_x, max_y]]
    return false unless points == corners

    area == (max_x - min_x) * (max_y - min_y)
  end

  alias_method :isRectangleCover, :is_rectangle_cover
end
