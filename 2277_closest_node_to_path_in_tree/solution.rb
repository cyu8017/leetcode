# LeetCode 2277 - Closest Node to Path in Tree
# https://leetcode.com/problems/closest-node-to-path-in-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} query
# @return {Integer[]}
def closest_node(n, edges, query)
  log = 17
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  up = Array.new(log) { Array.new(n, 0) }
  depth = Array.new(n, 0)
  dfs = lambda do |u, p|
    up[0][u] = p
    g[u].each do |v|
      next if v == p

      depth[v] = depth[u] + 1
      dfs.call(v, u)
    end
  end
  dfs.call(0, 0)
  (1...log).each do |k|
    n.times { |v| up[k][v] = up[k - 1][up[k - 1][v]] }
  end

  lift = lambda do |v, d|
    log.times { |k| v = up[k][v] if (d >> k) & 1 == 1 }
    v
  end

  lca = lambda do |a, b|
    a, b = b, a if depth[a] < depth[b]
    a = lift.call(a, depth[a] - depth[b])
    return a if a == b

    (log - 1).downto(0) do |k|
      if up[k][a] != up[k][b]
        a = up[k][a]
        b = up[k][b]
      end
    end
    up[0][a]
  end

  dist = lambda do |a, b|
    c = lca.call(a, b)
    depth[a] + depth[b] - 2 * depth[c]
  end

  query.map do |a, b, x|
    cands = [lca.call(a, b), lca.call(a, x), lca.call(b, x)]
    best = cands[0]
    best_d = dist.call(cands[0], x)
    (1...3).each do |t|
      d = dist.call(cands[t], x)
      if d < best_d
        best_d = d
        best = cands[t]
      end
    end
    best
  end
end

alias solve closest_node
