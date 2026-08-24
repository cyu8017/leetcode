# LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} disappear
# @return {Integer[]}
def minimum_time(n, edges, disappear)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  inf = 1 << 30
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    du, u = heap_pop_pair(pq)
    next if du > dist[u]
    g[u].each do |v, w|
      if dist[v] > dist[u] + w && dist[u] + w < disappear[v]
        dist[v] = dist[u] + w
        heap_push_pair(pq, [dist[v], v])
      end
    end
  end
  n.times.map { |i| dist[i] < disappear[i] ? dist[i] : -1 }
end

def heap_push_pair(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if cmp_pair(a[i], a[p]) >= 0
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop_pair(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp_pair(a[l], a[s]) < 0
      s = r if r < n && cmp_pair(a[r], a[s]) < 0
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end

def cmp_pair(a, b)
  a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
end
