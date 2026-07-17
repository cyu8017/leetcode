# LeetCode 1786 - Number of Restricted Paths From First to Last Node
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_restricted_paths(n, edges)
  adj = Array.new(n + 1) { [] }
  edges.each do |a, b, w|
    adj[a] << [b, w]
    adj[b] << [a, w]
  end
  dist = Array.new(n + 1, Float::INFINITY)
  dist[n] = 0
  heap = [[0, n]]
  push = lambda do |item|
    heap << item
    i = heap.length - 1
    while i > 0
      parent = (i - 1) / 2
      break if heap[parent][0] <= heap[i][0]
      heap[parent], heap[i] = heap[i], heap[parent]
      i = parent
    end
  end
  pop = lambda do
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      loop do
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = l if l < heap.length && heap[l][0] < heap[smallest][0]
        smallest = r if r < heap.length && heap[r][0] < heap[smallest][0]
        break if smallest == i
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
      end
    end
    top
  end
  until heap.empty?
    d, u = pop.call
    next if d != dist[u]
    adj[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        push.call([nd, v])
      end
    end
  end
  order = (1..n).sort_by { |u| dist[u] }
  mod = 1_000_000_007
  cnt = Array.new(n + 1, 0)
  cnt[n] = 1
  order.each do |u|
    next if u == n
    adj[u].each do |v, _w|
      cnt[u] = (cnt[u] + cnt[v]) % mod if dist[u] > dist[v]
    end
  end
  cnt[1]
end
