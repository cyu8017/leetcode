# LeetCode 3515 - Shortest Path in a Weighted Tree
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def tree_queries(n, edges, queries)
  g = Array.new(n + 1) { [] }
  weight = {}
  edges.each do |e|
    u, v, w = e[0], e[1], e[2]
    g[u] << [v, w]
    g[v] << [u, w]
    a = [u, v].min
    b = [u, v].max
    weight[(a << 32) | b] = w
  end
  in_t = Array.new(n + 1, 0)
  out_t = Array.new(n + 1, 0)
  dist = Array.new(n + 1, 0)
  parent = Array.new(n + 1, 0)
  time = [0]
  dfs = nil
  dfs = lambda do |u, p|
    in_t[u] = time[0]
    time[0] += 1
    g[u].each do |to, w|
      next if to == p
      parent[to] = u
      dist[to] = dist[u] + w
      dfs.call(to, u)
    end
    out_t[u] = time[0] - 1
  end
  dfs.call(1, 0)
  bit = Array.new(n + 2, 0)
  add = lambda do |i, v|
    while i <= n
      bit[i] += v
      i += i & -i
    end
  end
  range_add = lambda do |l, r, v|
    add.call(l + 1, v)
    add.call(r + 2, -v)
  end
  point = lambda do |i|
    s = 0
    i += 1
    while i > 0
      s += bit[i]
      i -= i & -i
    end
    s
  end
  (1..n).each { |i| range_add.call(in_t[i], in_t[i], dist[i]) }
  ans = []
  queries.each do |q|
    if q[0] == 1
      u, v, nw = q[1], q[2], q[3]
      a = [u, v].min
      b = [u, v].max
      key = (a << 32) | b
      ow = weight[key]
      delta = nw - ow
      weight[key] = nw
      child = parent[u] == v ? u : v
      range_add.call(in_t[child], out_t[child], delta)
    else
      ans << point.call(in_t[q[1]])
    end
  end
  ans
end
