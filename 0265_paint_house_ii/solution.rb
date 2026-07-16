# LeetCode 0265 - Paint House II
# https://leetcode.com/problems/paint-house-ii/

# @param {Integer[][]} costs
# @return {Integer}
def min_cost_ii(costs)
  return 0 if costs.empty?

  color_count = costs[0].length
  previous = costs[0].dup
  (1...costs.length).each do |row|
    min_cost = previous.min
    min_index = previous.index(min_cost)
    second_min = previous.each_with_index.filter_map { |value, index| index == min_index ? nil : value }.min
    current = Array.new(color_count) do |color|
      extra = color == min_index ? second_min : min_cost
      costs[row][color] + extra
    end
    previous = current
  end
  previous.min
end
