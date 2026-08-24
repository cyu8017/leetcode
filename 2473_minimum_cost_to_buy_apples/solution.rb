# LeetCode 2473 - Minimum Cost to Buy Apples
# https://leetcode.com/problems/minimum-cost-to-buy-apples/

# @param {Integer} n
# @param {Integer[][]} roads
# @param {Integer[]} apple_cost
# @param {Integer} k
# @return {Integer[]}
def min_cost(n, roads, apple_cost, k)
  g = Array.new(n + 1) { [] }
  roads.each do |r|
    g[r[0]] << [r[1], r[2]]
    g[r[1]] << [r[0], r[2]]
  end

  heap_push = lambda do |heap, item|
    heap << item
    i = heap.length - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] <= heap[i]

      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  heap_pop = lambda do |heap|
    top = heap[0]
    last = heap.pop
    return top if heap.empty?

    heap[0] = last
    i = 0
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left] < heap[smallest]
      smallest = right if right < heap.length && heap[right] < heap[smallest]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  ans = Array.new(n, 0)
  inf = 10**18
  (1..n).each do |start|
    dist = Array.new(n + 1, inf)
    dist[start] = 0
    pq = [[0, start]]
    until pq.empty?
      d, u = heap_pop.call(pq)
      next if d != dist[u]

      g[u].each do |v, w|
        nd = d + w
        if nd < dist[v]
          dist[v] = nd
          heap_push.call(pq, [nd, v])
        end
      end
    end
    best = inf
    (1..n).each do |city|
      cost = dist[city] * (k + 1) + apple_cost[city - 1]
      best = cost if cost < best
    end
    ans[start - 1] = best
  end
  ans
end
