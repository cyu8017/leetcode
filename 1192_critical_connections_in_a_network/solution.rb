# LeetCode 1192 - Critical Connections in a Network
# https://leetcode.com/problems/critical-connections-in-a-network/

# @param {Integer} n
# @param {Integer[][]} connections
# @return {Integer[][]}
def critical_connections(n, connections)
  graph = Hash.new { |h, k| h[k] = [] }
  connections.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  disc = Array.new(n, -1)
  low = Array.new(n, -1)
  time = 0
  bridges = []
  dfs = nil
  dfs = lambda do |node, parent|
    disc[node] = low[node] = time
    time += 1
    graph[node].each do |nxt|
      next if nxt == parent
      if disc[nxt] == -1
        dfs.call(nxt, node)
        low[node] = [low[node], low[nxt]].min
        bridges << [node, nxt] if low[nxt] > disc[node]
      else
        low[node] = [low[node], disc[nxt]].min
      end
    end
  end
  dfs.call(0, -1)
  bridges.map { |a, b| [[a, b].min, [a, b].max] }
end
