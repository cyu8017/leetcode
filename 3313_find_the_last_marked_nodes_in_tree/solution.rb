# LeetCode 3313 - Find the Last Marked Nodes in Tree
# https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

# @param {Integer[][]} g
# @param {Integer} start
# @return {Array}
def last_marked_bfs(g, start)
  n = g.length
  dist = Array.new(n, -1)
  q = [start]
  dist[start] = 0
  far = start
  qi = 0
  while qi < q.length
    u = q[qi]
    qi += 1
    far = u if dist[u] > dist[far]
    g[u].each do |v|
      if dist[v] == -1
        dist[v] = dist[u] + 1
        q << v
      end
    end
  end
  [far, dist]
end

# @param {Integer[][]} edges
# @return {Integer[]}
def last_marked_nodes(edges)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  u = last_marked_bfs(g, 0)[0]
  v, du = last_marked_bfs(g, u)
  dv = last_marked_bfs(g, v)[1]
  n.times.map { |i| du[i] >= dv[i] ? u : v }
end
