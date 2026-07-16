# LeetCode 0492 - Construct the Rectangle
# https://leetcode.com/problems/construct-the-rectangle/

class Solution
  def construct_rectangle(area)
    width = Math.sqrt(area).to_i
    while width.positive?
      if area % width == 0
        return [area / width, width]
      end
      width -= 1
    end
    [area, 1]
  end

  alias_method :constructRectangle, :construct_rectangle
end
