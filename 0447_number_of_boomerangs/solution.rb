# LeetCode 0447 - Number of Boomerangs
# https://leetcode.com/problems/number-of-boomerangs/

class Solution
  def number_of_boomerangs(points)
    total = 0
    points.each do |anchor|
      distances = Hash.new(0)
      points.each do |other|
        dx = anchor[0] - other[0]
        dy = anchor[1] - other[1]
        distance = dx * dx + dy * dy
        distances[distance] += 1
      end
      distances.each_value do |count|
        total += count * (count - 1)
      end
    end
    total
  end

  alias_method :numberOfBoomerangs, :number_of_boomerangs
end
