# LeetCode 0802 - Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/

# @param {Integer[][]} graph
# @return {Integer[]}
def eventual_safe_nodes(graph)
  n = graph.length
  color = Array.new(n, 0)

  dfs = lambda do |node|
    return color[node] == 2 if color[node] != 0

    color[node] = 1
    graph[node].each { |nei| return false unless dfs.call(nei) }
    color[node] = 2
    true
  end

  (0...n).select { |i| dfs.call(i) }
end
