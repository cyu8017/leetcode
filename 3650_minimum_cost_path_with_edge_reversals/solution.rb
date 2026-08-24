# LeetCode 3650 - Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_cost(n, edges)
  g = Array.new(n) { [] }
  edges.each do |u, v, w|
    g[u] << [v, w]
    g[v] << [u, w * 2]
  end
  inf = 1073741823
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    pq.sort_by! { |x| x[0] }
    d, u = pq.shift
    next if d > dist[u]
    return d if u == n - 1

    g[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        pq << [nd, v]
      end
    end
  end
  -1
end
