# LeetCode 3585 - Find Weighted Median Node in Tree
# https://leetcode.com/problems/find-weighted-median-node-in-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def find_median(n, edges, queries)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    u, v = q[0], q[1]
    parent = Array.new(n, -2)
    pw = Array.new(n, 0)
    parent[u] = -1
    dq = [u]
    until dq.empty?
      x = dq.shift
      break if x == v
      g[x].each do |to, w|
        if parent[to] == -2
          parent[to] = x
          pw[to] = w
          dq << to
        end
      end
    end
    nodes = [v]
    weights = []
    cur = v
    while cur != u
      weights << pw[cur]
      cur = parent[cur]
      nodes << cur
    end
    nodes.reverse!
    weights.reverse!
    total = 0
    weights.each { |w| total += w }
    need = (total + 1) / 2
    sm = 0
    med = u
    weights.each_with_index do |w, i|
      sm += w
      med = nodes[i + 1]
      break if sm >= need
    end
    ans[qi] = med
  end
  ans
end
