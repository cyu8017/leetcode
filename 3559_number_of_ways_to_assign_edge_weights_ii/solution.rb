# LeetCode 3559 - Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def assign_edge_weights(edges, queries)
  mod = 1000000007
  log = 17
  n = edges.length + 1
  depth = Array.new(n + 1, 0)
  graph = Array.new(n + 1) { [] }
  parent = Array.new(log) { Array.new(n + 1, -1) }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  dfs = nil
  dfs = lambda do |u, p|
    parent[0][u] = p
    graph[u].each do |v|
      if v != p
        depth[v] = depth[u] + 1
        dfs.call(v, u)
      end
    end
  end
  lca = lambda do |u, v|
    u, v = v, u if depth[u] < depth[v]
    (log - 1).downto(0) do |k|
      u = parent[k][u] if parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]
    end
    return u if u == v
    (log - 1).downto(0) do |k|
      if parent[k][u] != -1 && parent[k][u] != parent[k][v]
        u = parent[k][u]
        v = parent[k][v]
      end
    end
    parent[0][u]
  end
  mod_pow = lambda do |exp|
    base = 2
    res = 1
    while exp > 0
      res = res * base % mod if (exp & 1) != 0
      base = base * base % mod
      exp >>= 1
    end
    res
  end
  dfs.call(1, -1)
  (1...log).each do |k|
    (1..n).each do |v|
      parent[k][v] = parent[k - 1][parent[k - 1][v]] if parent[k - 1][v] != -1
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    u, v = q[0], q[1]
    if u == v
      ans[i] = 0
      next
    end
    a = lca.call(u, v)
    d = depth[u] + depth[v] - 2 * depth[a]
    ans[i] = mod_pow.call(d - 1)
  end
  ans
end
