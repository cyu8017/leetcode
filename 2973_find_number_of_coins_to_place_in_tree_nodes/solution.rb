# LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

# @param {Integer[][]} edges
# @param {Integer[]} cost
# @return {Integer[]}
def placed_coins(edges, cost)
  n = cost.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = Array.new(n, 0)
  dfs = lambda do |u, p|
    vals = [cost[u]]
    g[u].each do |v|
      next if v == p

      vals += dfs.call(v, u)
    end
    vals.sort!
    if vals.length < 3
      ans[u] = 1
    else
      m = vals.length
      cand1 = vals[m - 1] * vals[m - 2] * vals[m - 3]
      cand2 = vals[0] * vals[1] * vals[m - 1]
      best = [cand1, cand2].max
      best = 0 if best < 0
      ans[u] = best
    end
    return vals if vals.length <= 5

    [vals[0], vals[1], vals[-3], vals[-2], vals[-1]]
  end
  dfs.call(0, -1)
  ans
end
