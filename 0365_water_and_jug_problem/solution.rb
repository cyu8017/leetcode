# LeetCode 0365 - Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/

class Solution
  def can_measure_water(x, y, target)
    return true if target.zero?
    return false if x + y < target

    target % x.gcd(y) == 0
  end

  alias_method :canMeasureWater, :can_measure_water
end
