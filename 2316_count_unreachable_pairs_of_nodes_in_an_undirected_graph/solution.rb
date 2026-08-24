# LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_pairs(n, edges)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  vis = Array.new(n, false)
  dfs = lambda do |u|
    vis[u] = true
    size = 1
    g[u].each { |v| size += dfs.call(v) unless vis[v] }
    size
  end
  ans = 0
  seen = 0
  (0...n).each do |i|
    next if vis[i]
    sz = dfs.call(i)
    ans += sz * seen
    seen += sz
  end
  ans
end
