# LeetCode 0478 - Generate Random Point in a Circle
# https://leetcode.com/problems/generate-random-point-in-a-circle/

$uniform = nil

def set_uniform(fn)
  $uniform = fn
end

class Solution
  def initialize(radius, x_center, y_center)
    @radius = radius.to_f
    @x_center = x_center.to_f
    @y_center = y_center.to_f
  end

  def randPoint
    loop do
      x = $uniform.call(-@radius, @radius)
      y = $uniform.call(-@radius, @radius)
      if x * x + y * y <= @radius * @radius
        return [(@x_center + x).round(5), (@y_center + y).round(5)]
      end
    end
  end
end
