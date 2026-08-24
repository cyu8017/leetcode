# LeetCode 3977 - Minimum Time to Reach Target With Limited Power
# https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} power
# @param {Integer[]} cost
# @param {Integer} source
# @param {Integer} target
# @return {Integer[]}
def min_time_max_power(n, edges, power, cost, source, target)
  inf = 2**62
  g = Array.new(n) { [] }
  edges.each { |e| g[e[0]] << [e[1], e[2]] }
  dist = Array.new(n) { Array.new(power + 1, inf) }
  pq = [[0, -power, source]]
  dist[source][power] = 0
  until pq.empty?
    pq.sort_by! { |a| [a[0], a[1]] }
    d, neg_p, u = pq.shift
    p = -neg_p
    return [d, p] if u == target
    next if d > dist[u][p] || p < cost[u]
    p -= cost[u]
    g[u].each do |v, t|
      nd = d + t
      if nd < dist[v][p]
        dist[v][p] = nd
        pq << [nd, -p, v]
      end
    end
  end
  [-1, -1]
end
