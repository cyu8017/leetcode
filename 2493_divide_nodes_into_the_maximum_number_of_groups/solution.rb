# LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def magnificent_sets(n, edges)
  g = Array.new(n + 1) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end

  bfs_depth = lambda do |start|
    dist = Array.new(n + 1, -1)
    q = [start]
    dist[start] = 1
    best = 1
    until q.empty?
      u = q.shift
      best = dist[u] if dist[u] > best
      g[u].each do |v|
        if dist[v] == -1
          dist[v] = dist[u] + 1
          q << v
        end
      end
    end
    best
  end

  color = Array.new(n + 1, -1)
  components = []
  (1..n).each do |i|
    next if color[i] != -1

    comp = []
    q = [i]
    color[i] = 0
    bipartite = true
    until q.empty?
      u = q.shift
      comp << u
      g[u].each do |v|
        if color[v] == -1
          color[v] = color[u] ^ 1
          q << v
        elsif color[v] == color[u]
          bipartite = false
        end
      end
    end
    return -1 unless bipartite

    components << comp
  end
  ans = 0
  components.each do |comp|
    best = 0
    comp.each { |u| best = [best, bfs_depth.call(u)].max }
    ans += best
  end
  ans
end
