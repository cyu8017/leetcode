# LeetCode 0475 - Heaters
# https://leetcode.com/problems/heaters/

class Solution
  def find_radius(houses, heaters)
    sorted_heaters = heaters.sort
    radius = 0
    houses.each do |house|
      position = sorted_heaters.bsearch_index { |heater| heater >= house } || sorted_heaters.length
      distances = []
      distances << (sorted_heaters[position] - house).abs if position < sorted_heaters.length
      distances << (sorted_heaters[position - 1] - house).abs if position.positive?
      radius = [radius, distances.min].max
    end
    radius
  end

  alias_method :findRadius, :find_radius
end
