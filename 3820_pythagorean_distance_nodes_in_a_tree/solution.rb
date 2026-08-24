# LeetCode 3820 - Pythagorean Distance Nodes in a Tree
# https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def special_nodes(n, edges, x, y, z)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  bfs = lambda do |start|
    dist = Array.new(n, 1_000_000_000)
    q = [start]
    dist[start] = 0
    qi = 0
    while qi < q.length
      u = q[qi]
      qi += 1
      g[u].each do |v|
        if dist[v] > dist[u] + 1
          dist[v] = dist[u] + 1
          q << v
        end
      end
    end
    dist
  end
  d1 = bfs.call(x)
  d2 = bfs.call(y)
  d3 = bfs.call(z)
  ans = 0
  (0...n).each do |i|
    a = [d1[i], d2[i], d3[i]].sort
    x0, x1, x2 = a[0], a[1], a[2]
    ans += 1 if x0 * x0 + x1 * x1 == x2 * x2
  end
  ans
end
