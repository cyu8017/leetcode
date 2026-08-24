# LeetCode 3772 - Maximum Subgraph Score in a Tree
# https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} good
# @return {Integer[]}
def max_subgraph_score(n, edges, good)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  parent = Array.new(n, -2)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    g[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        order << v
      end
    end
    i += 1
  end
  down = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    u = order[i]
    down[u] = 2 * good[u] - 1
    g[u].each { |v| down[u] += down[v] if parent[v] == u && down[v] > 0 }
  end
  ans = down.dup
  order.each do |u|
    g[u].each do |v|
      next unless parent[v] == u
      outside = ans[u]
      outside -= down[v] if down[v] > 0
      ans[v] = down[v]
      ans[v] += outside if outside > 0
    end
  end
  ans
end
