# LeetCode 1774 - Closest Dessert Cost
# https://leetcode.com/problems/closest-dessert-cost/

# @param {Integer[]} base_costs
# @param {Integer[]} topping_costs
# @param {Integer} target
# @return {Integer}
def closest_cost(base_costs, topping_costs, target)
  best = Float::INFINITY

  dfs = lambda do |i, cur|
    if (cur - target).abs < (best - target).abs ||
       ((cur - target).abs == (best - target).abs && cur < best)
      best = cur
    end
    return if i == topping_costs.length || cur >= target

    dfs.call(i + 1, cur)
    dfs.call(i + 1, cur + topping_costs[i])
    dfs.call(i + 1, cur + 2 * topping_costs[i])
  end

  base_costs.each { |base| dfs.call(0, base) }
  best
end
