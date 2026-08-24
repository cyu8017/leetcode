# LeetCode 3789 - Minimum Cost to Acquire Required Items
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

# @param {Integer} cost1
# @param {Integer} cost2
# @param {Integer} cost_both
# @param {Integer} need1
# @param {Integer} need2
# @return {Integer}
def minimum_cost(cost1, cost2, cost_both, need1, need2)
  a = need1 * cost1 + need2 * cost2
  b = cost_both * [need1, need2].max
  mn = [need1, need2].min
  c = cost_both * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
  [a, b, c].min
end
