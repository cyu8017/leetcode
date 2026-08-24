# LeetCode 3787 - Find Diameter Endpoints of a Tree
# https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {String}
def find_special_nodes(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  bfs = lambda do |start|
    dist = Array.new(n, -1)
    dist[start] = 0
    q = [start]
    far = start
    head = 0
    while head < q.length
      u = q[head]
      head += 1
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
  a, = bfs.call(0)
  b, dist1 = bfs.call(a)
  _, dist2 = bfs.call(b)
  d = dist1[b]
  ans = Array.new(n, "0")
  (0...n).each { |i| ans[i] = "1" if dist1[i] == d || dist2[i] == d }
  ans.join
end
