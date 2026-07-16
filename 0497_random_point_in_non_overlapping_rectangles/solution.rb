# LeetCode 0497 - Random Point in Non-overlapping Rectangles
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

$uniform = nil

def set_uniform(fn)
  $uniform = fn
end

class Solution
  def initialize(rects)
    @rects = rects
    @total = 0
    rects.each do |a, b, x, y|
      @total += (x - a + 1) * (y - b + 1)
    end
  end

  def pick
    index = $uniform.call(0, @total).to_i
    index = @total - 1 if index >= @total
    @rects.each do |a, b, x, y|
      width = x - a + 1
      height = y - b + 1
      size = width * height
      if index < size
        offset_x = index % width
        offset_y = index / width
        return [a + offset_x, b + offset_y]
      end
      index -= size
    end
    last = @rects[-1]
    [last[0], last[1]]
  end
end
