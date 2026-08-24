# LeetCode 3558 - Number of Ways to Assign Edge Weights I
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

# @param {Integer[][]} edges
# @return {Integer}
def assign_edge_weights(edges)
  mod = 1000000007
  n = edges.length + 1
  g = Array.new(n + 1) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  dfs = nil
  dfs = lambda do |i, fa|
    res = 0
    g[i].each do |j|
      res = [res, dfs.call(j, i) + 1].max if j != fa
    end
    res
  end
  pow2 = lambda do |exp|
    a = 2
    res = 1
    while exp > 0
      res = res * a % mod if (exp & 1) != 0
      a = a * a % mod
      exp >>= 1
    end
    res
  end
  pow2.call(dfs.call(1, 0) - 1)
end
