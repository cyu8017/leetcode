# LeetCode 2039 - The Time When the Network Becomes Idle
# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

# @param {Integer[][]} edges
# @param {Integer[]} patience
# @return {Integer}
def network_becomes_idle(edges, patience)
  n = patience.length
  g = Array.new(n) { [] }
  edges.each do |u, v|
    g[u] << v
    g[v] << u
  end
  dist = Array.new(n, -1)
  q = [0]
  dist[0] = 0
  until q.empty?
    u = q.shift
    g[u].each do |v|
      next unless dist[v] == -1

      dist[v] = dist[u] + 1
      q << v
    end
  end
  ans = 0
  (1...n).each do |i|
    rnd = dist[i] * 2
    last_send = ((rnd - 1) / patience[i]) * patience[i]
    ans = [ans, last_send + rnd].max
  end
  ans + 1
end
