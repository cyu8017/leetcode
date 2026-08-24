# LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def minimum_weight(edges, queries)
  log = 17
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  parent = Array.new(log) { Array.new(n, -1) }
  depth = Array.new(n, 0)
  dist = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |u, p|
    parent[0][u] = p
    g[u].each do |to, w|
      next if to == p
      depth[to] = depth[u] + 1
      dist[to] = dist[u] + w
      dfs.call(to, u)
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
  path = lambda do |u, v|
    a = lca.call(u, v)
    dist[u] + dist[v] - 2 * dist[a]
  end
  dfs.call(0, -1)
  (1...log).each do |k|
    (0...n).each do |v|
      parent[k][v] = parent[k - 1][parent[k - 1][v]] if parent[k - 1][v] != -1
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    a, b, c = q[0], q[1], q[2]
    ans[i] = (path.call(a, b) + path.call(b, c) + path.call(a, c)) / 2
  end
  ans
end
