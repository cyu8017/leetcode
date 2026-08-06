# LeetCode 1976 - Number of Ways to Arrive at Destination
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def count_paths(n, roads)
  mod = 10**9 + 7
  g = Array.new(n) { [] }
  roads.each do |u, v, t|
    g[u] << [v, t]
    g[v] << [u, t]
  end
  dist = Array.new(n, Float::INFINITY)
  ways = Array.new(n, 0)
  dist[0] = 0
  ways[0] = 1
  pq = [[0, 0]]

  push = lambda do |item|
    pq << item
    i = pq.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if pq[p][0] <= pq[i][0]
      pq[p], pq[i] = pq[i], pq[p]
      i = p
    end
  end

  pop = lambda do
    top = pq[0]
    last = pq.pop
    return top if pq.empty?
    pq[0] = last
    i = 0
    loop do
      smallest = i
      l = 2 * i + 1
      r = 2 * i + 2
      smallest = l if l < pq.length && pq[l][0] < pq[smallest][0]
      smallest = r if r < pq.length && pq[r][0] < pq[smallest][0]
      break if smallest == i
      pq[smallest], pq[i] = pq[i], pq[smallest]
      i = smallest
    end
    top
  end

  until pq.empty?
    d, u = pop.call
    next if d > dist[u]
    g[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        ways[v] = ways[u]
        push.call([nd, v])
      elsif nd == dist[v]
        ways[v] = (ways[v] + ways[u]) % mod
      end
    end
  end
  ways[n - 1]
end
