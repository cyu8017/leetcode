# LeetCode 3973 - Distinct Gate Paths to LCA
# https://leetcode.com/problems/distinct-gate-paths-to-lca/

# @param {Integer} n
# @param {Integer[]} parent
# @param {Integer[][]} gates
# @param {Integer[][]} queries
# @return {Integer}
def gate_path_xor(n, parent, gates, queries)
  mod = 1_000_000_007
  multiply = lambda do |a, b|
    c = [[0, 0], [0, 0]]
    2.times do |i|
      2.times do |j|
        2.times do |k|
          c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
        end
      end
    end
    c
  end
  logn = 1
  logn += 1 while (1 << logn) <= n
  up = Array.new(logn) { Array.new(n, 0) }
  product = Array.new(logn) { Array.new(n) }
  children = Array.new(n) { [] }
  (1...n).each { |node| children[parent[node]] << node }
  depth = Array.new(n, 0)
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    children[u].each do |v|
      depth[v] = depth[u] + 1
      order << v
    end
    i += 1
  end
  n.times do |u|
    up[0][u] = u == 0 ? 0 : parent[u]
    product[0][u] = [[gates[u][1], gates[u][2]], [gates[u][2], gates[u][0]]]
  end
  (1...logn).each do |level|
    n.times do |u|
      mid = up[level - 1][u]
      up[level][u] = up[level - 1][mid]
      product[level][u] = multiply.call(product[level - 1][u], product[level - 1][mid])
    end
  end
  lift_node = lambda do |node, distance|
    level = 0
    while distance > 0
      node = up[level][node] if (distance & 1) != 0
      distance >>= 1
      level += 1
    end
    node
  end
  lca = lambda do |a, b|
    if depth[a] > depth[b]
      a = lift_node.call(a, depth[a] - depth[b])
    elsif depth[b] > depth[a]
      b = lift_node.call(b, depth[b] - depth[a])
    end
    return a if a == b
    (logn - 1).downto(0) do |level|
      if up[level][a] != up[level][b]
        a = up[level][a]
        b = up[level][b]
      end
    end
    up[0][a]
  end
  ways = lambda do |node, card, distance|
    vector = [0, 0]
    vector[card] = 1
    level = 0
    while distance > 0
      if (distance & 1) != 0
        matrix = product[level][node]
        vector = [
          (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % mod,
          (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % mod
        ]
        node = up[level][node]
      end
      distance >>= 1
      level += 1
    end
    (vector[0] + vector[1]) % mod
  end
  answer = 0
  queries.each do |query|
    ancestor = lca.call(query[0], query[2])
    alice = ways.call(query[0], query[1], depth[query[0]] - depth[ancestor])
    bob = ways.call(query[2], query[3], depth[query[2]] - depth[ancestor])
    total = (alice * bob) % mod
    answer ^= total
  end
  answer
end
