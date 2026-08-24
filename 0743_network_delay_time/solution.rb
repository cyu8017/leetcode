# LeetCode 0743 - Network Delay Time
# https://leetcode.com/problems/network-delay-time/

# @param {Integer[][]} times
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def network_delay_time(times, n, k)
  graph = Hash.new { |h, key| h[key] = [] }
  times.each { |u, v, w| graph[u] << [v, w] }

  dist = {}
  (1..n).each { |node| dist[node] = Float::INFINITY }
  dist[k] = 0
  heap = [[0, k]]

  heap_push = lambda do |item|
    heap << item
    i = heap.length - 1
    while i > 0
      parent = (i - 1) / 2
      break if heap[parent][0] <= heap[i][0]

      heap[parent], heap[i] = heap[i], heap[parent]
      i = parent
    end
  end

  heap_pop = lambda do
    last = heap.pop
    return last if heap.empty?

    top = heap[0]
    heap[0] = last
    i = 0
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left][0] < heap[smallest][0]
      smallest = right if right < heap.length && heap[right][0] < heap[smallest][0]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  until heap.empty?
    d, node = heap_pop.call
    next if d > dist[node]

    graph[node].each do |nei, weight|
      nd = d + weight
      if nd < dist[nei]
        dist[nei] = nd
        heap_push.call([nd, nei])
      end
    end
  end

  ans = dist.values.max
  ans == Float::INFINITY ? -1 : ans.to_i
end
