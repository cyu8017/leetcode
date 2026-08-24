# LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} cost
# @return {Integer}
def min_increase(n, edges, cost)
  graph = Array.new(n) { [] }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  ans = [0]
  dfs = nil
  dfs = lambda do |u, p|
    return cost[u] if graph[u].length == 1 && p != -1
    child_vals = []
    graph[u].each do |v|
      next if v == p
      child_vals << dfs.call(v, u)
    end
    return cost[u] if child_vals.empty?
    mx = child_vals.max
    child_vals.each { |c| ans[0] += 1 if c < mx }
    mx + cost[u]
  end
  dfs.call(0, -1)
  ans[0]
end
