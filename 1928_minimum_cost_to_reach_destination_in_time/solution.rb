# LeetCode 1928 - Minimum Cost to Reach Destination in Time
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

# @param {Integer} max_time
# @param {Integer[][]} edges
# @param {Integer[]} passing_fee
# @return {Integer}
def min_cost(max_time, edges, passing_fee)
  n = passing_fee.length
  graph = Array.new(n) { [] }
  edges.each do |u, v, t|
    graph[u] << [v, t]
    graph[v] << [u, t]
  end
  min_time = Array.new(n, max_time + 1)
  pq = [[passing_fee[0], 0, 0]]

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
    cost, time, u = pop.call
    next if time >= min_time[u]
    min_time[u] = time
    return cost if u == n - 1
    graph[u].each do |v, dt|
      nt = time + dt
      push.call([cost + passing_fee[v], nt, v]) if nt <= max_time && nt < min_time[v]
    end
  end
  -1
end
