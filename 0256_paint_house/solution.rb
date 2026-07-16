# LeetCode 0256 - Paint House
# https://leetcode.com/problems/paint-house/

# @param {Integer[][]} costs
# @return {Integer}
def min_cost(costs)
  return 0 if costs.empty?

  previous = costs[0].dup
  (1...costs.length).each do |row|
    previous = [
      costs[row][0] + [previous[1], previous[2]].min,
      costs[row][1] + [previous[0], previous[2]].min,
      costs[row][2] + [previous[0], previous[1]].min,
    ]
  end
  previous.min
end
