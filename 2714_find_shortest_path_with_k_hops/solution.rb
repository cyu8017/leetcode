# LeetCode 2714 - Find Shortest Path With K Hops
# https://leetcode.com/problems/find-shortest-path-with-k-hops/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} s
# @param {Integer} d
# @param {Integer} k
# @return {Integer}
def shortest_path_with_hops(n, edges, s, d, k)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  inf = 10**18
  dist = Array.new(n) { Array.new(k + 1, inf) }
  dist[s][0] = 0
  pq = [[0, s, 0]]
  until pq.empty?
    pq.sort_by! { |x| x[0] }
    cd, u, hops = pq.shift
    return cd if u == d
    next if cd > dist[u][hops]

    g[u].each do |to, w|
      if cd + w < dist[to][hops]
        dist[to][hops] = cd + w
        pq << [dist[to][hops], to, hops]
      end
      if hops < k && cd < dist[to][hops + 1]
        dist[to][hops + 1] = cd
        pq << [cd, to, hops + 1]
      end
    end
  end
  -1
end

def solve(*args)
  shortest_path_with_hops(*args)
end
