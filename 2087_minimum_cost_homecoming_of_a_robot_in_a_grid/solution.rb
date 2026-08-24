# LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

# @param {Integer[]} start_pos
# @param {Integer[]} home_pos
# @param {Integer[]} row_costs
# @param {Integer[]} col_costs
# @return {Integer}
def min_cost(start_pos, home_pos, row_costs, col_costs)
  ans = 0
  sr, sc = start_pos
  hr, hc = home_pos
  if sr < hr
    (sr + 1).upto(hr) { |r| ans += row_costs[r] }
  else
    (sr - 1).downto(hr) { |r| ans += row_costs[r] }
  end
  if sc < hc
    (sc + 1).upto(hc) { |c| ans += col_costs[c] }
  else
    (sc - 1).downto(hc) { |c| ans += col_costs[c] }
  end
  ans
end
