# LeetCode 1473 - Paint House Iii
# https://leetcode.com/problems/paint-house-iii/

def min_cost(houses, cost, m, n, target)
  inf = 10**15
  dp = { [0, 0] => 0 }
  houses.each_with_index do |painted, i|
    nxt = {}
    colors = painted != 0 ? [painted] : (1..n).to_a
    dp.each do |(prev, groups), value|
      colors.each do |color|
        ng = groups + (color != prev ? 1 : 0)
        next if ng > target
        nv = value + (painted != 0 ? 0 : cost[i][color - 1])
        key = [color, ng]
        nxt[key] = [nxt.fetch(key, inf), nv].min
      end
    end
    dp = nxt
  end
  ans = dp.select { |(_c, g), _v| g == target }.values.min || inf
  ans == inf ? -1 : ans
end
