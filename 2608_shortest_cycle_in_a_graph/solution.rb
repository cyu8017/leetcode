# LeetCode 2608 - Shortest Cycle in a Graph
# https://leetcode.com/problems/shortest-cycle-in-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_shortest_cycle(n, edges)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  inf = 1_000_000_000
  ans = inf
  n.times do |start|
    dist = Array.new(n, -1)
    parent = Array.new(n, -1)
    q = [start]
    dist[start] = 0
    until q.empty?
      u = q.shift
      g[u].each do |v|
        if dist[v] < 0
          dist[v] = dist[u] + 1
          parent[v] = u
          q << v
        elsif parent[u] != v
          c = dist[u] + dist[v] + 1
          ans = c if c < ans
        end
      end
    end
  end
  ans == inf ? -1 : ans
end
