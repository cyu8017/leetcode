# LeetCode 3123 - Find Edges in Shortest Paths
# https://leetcode.com/problems/find-edges-in-shortest-paths/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean[]}
def find_answer(n, edges)
  g = Array.new(n) { [] }
  edges.each_with_index do |(a, b, w), i|
    g[a] << [b, w, i]
    g[b] << [a, w, i]
  end
  inf = 1 << 30
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    da, a = heap_pop_pair(pq)
    next if da > dist[a]
    g[a].each do |b, w, _|
      if dist[b] > dist[a] + w
        dist[b] = dist[a] + w
        heap_push_pair(pq, [dist[b], b])
      end
    end
  end
  ans = Array.new(edges.length, false)
  return ans if dist[n - 1] == inf
  q = [n - 1]
  until q.empty?
    a = q.shift
    g[a].each do |b, w, i|
      if dist[a] == dist[b] + w
        ans[i] = true
        q << b
      end
    end
  end
  ans
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
