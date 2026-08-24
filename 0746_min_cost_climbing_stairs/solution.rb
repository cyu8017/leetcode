# LeetCode 0746 - Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

# @param {Integer[]} cost
# @return {Integer}
def min_cost_climbing_stairs(cost)
  a = 0
  b = 0
  cost.reverse_each do |c|
    a, b = c + [a, b].min, a
  end
  [a, b].min
end
