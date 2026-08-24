# LeetCode 3502 - Minimum Cost to Reach Every Position
# https://leetcode.com/problems/minimum-cost-to-reach-every-position/

# @param {Integer[]} cost
# @return {Integer[]}
def min_costs(cost)
  n = cost.length
  ans = Array.new(n, 0)
  mi = cost[0]
  (0...n).each do |i|
    mi = [mi, cost[i]].min
    ans[i] = mi
  end
  ans
end
