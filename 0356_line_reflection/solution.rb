# LeetCode 0356 - Line Reflection
# https://leetcode.com/problems/line-reflection/

class Solution
  def is_reflected(points)
    point_set = points.map { |x, y| [x, y] }.to_h { |point| [point, true] }
    xs = points.map(&:first)
    min_x = xs.min
    max_x = xs.max
    target = min_x + max_x

    points.each do |x, y|
      return false unless point_set.key?([target - x, y])
    end

    true
  end

  alias_method :isReflected, :is_reflected
end
