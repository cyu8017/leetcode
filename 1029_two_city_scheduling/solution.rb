# LeetCode 1029 - Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/

# @param {Integer[][]} costs
# @return {Integer}
def two_city_sched_cost(costs)
  costs = costs.sort_by { |c| c[0] - c[1] }
  half = costs.length / 2
  costs[0...half].sum { |c| c[0] } + costs[half..].sum { |c| c[1] }
end
