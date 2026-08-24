# LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def min_operations_queries(n, edges, queries)
  log = 15
  g = Array.new(n) { [] }
  edges.each do |a, b, w|
    g[a] << [b, w]
    g[b] << [a, w]
  end
  up = Array.new(log) { Array.new(n, 0) }
  depth = Array.new(n, 0)
  cnt = Array.new(n) { Array.new(27, 0) }

  dfs = lambda do |u, p|
    up[0][u] = p
    g[u].each do |v, w|
      next if v == p

      depth[v] = depth[u] + 1
      (0...27).each { |i| cnt[v][i] = cnt[u][i] }
      cnt[v][w] += 1
      dfs.call(v, u)
    end
  end

  dfs.call(0, 0)
  (1...log).each do |j|
    (0...n).each { |i| up[j][i] = up[j - 1][up[j - 1][i]] }
  end

  lca = lambda do |a, b|
    a, b = b, a if depth[a] < depth[b]
    diff = depth[a] - depth[b]
    (0...log).each { |j| a = up[j][a] if (diff & (1 << j)) != 0 }
    return a if a == b

    (log - 1).downto(0) do |j|
      if up[j][a] != up[j][b]
        a = up[j][a]
        b = up[j][b]
      end
    end
    up[0][a]
  end

  queries.map do |a, b|
    c = lca.call(a, b)
    total = depth[a] + depth[b] - 2 * depth[c]
    best = 0
    (1...27).each do |w|
      f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
      best = f if f > best
    end
    total - best
  end
end
