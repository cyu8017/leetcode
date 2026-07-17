# LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_trio_degree(n, edges)
  adj = Array.new(n) { Array.new(n, false) }
  degree = Array.new(n, 0)
  edges.each do |a, b|
    u = a - 1
    v = b - 1
    adj[u][v] = true
    adj[v][u] = true
    degree[u] += 1
    degree[v] += 1
  end
  best = Float::INFINITY
  edges.each do |a, b|
    u = a - 1
    v = b - 1
    (0...n).each do |k|
      if adj[u][k] && adj[v][k]
        total = degree[u] + degree[v] + degree[k] - 6
        best = total if total < best
      end
    end
  end
  best == Float::INFINITY ? -1 : best
end
