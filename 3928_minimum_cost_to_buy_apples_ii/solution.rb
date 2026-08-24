# LeetCode 3928 - Minimum Cost to Buy Apples II
# https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

# @param {Integer} n
# @param {Integer[]} prices
# @param {Integer[][]} roads
# @return {Integer[]}
def min_cost_to_buy_apples(n, prices, roads)
  dijkstra = lambda do |source, carrying, inf|
    dist = Array.new(n, inf)
    dist[source] = 0
    pq = [[0, source]]
    until pq.empty?
      pq.sort_by! { |a| a[0] }
      d, node = pq.shift
      next if d != dist[node]
      g[node].each do |e|
        weight = carrying ? e[:full] : e[:empty]
        nxt = d + weight
        if nxt < dist[e[:to]]
          dist[e[:to]] = nxt
          pq << [nxt, e[:to]]
        end
      end
    end
    dist
  end
  g = Array.new(n) { [] }
  roads.each do |road|
    empty = road[2]
    full = road[2] * road[3]
    g[road[0]] << { to: road[1], empty: empty, full: full }
    g[road[1]] << { to: road[0], empty: empty, full: full }
  end
  inf = 1 << 62
  answer = Array.new(n, 0)
  n.times do |source|
    empty_dist = dijkstra.call(source, false, inf)
    full_dist = dijkstra.call(source, true, inf)
    best = prices[source]
    n.times do |shop|
      next if empty_dist[shop] == inf || full_dist[shop] == inf
      total = empty_dist[shop] + full_dist[shop] + prices[shop]
      best = total if total < best
    end
    answer[source] = best
  end
  answer
end
