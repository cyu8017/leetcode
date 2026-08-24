# LeetCode 2737 - Find the Closest Marked Node
# https://leetcode.com/problems/find-the-closest-marked-node/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} s
# @param {Integer[]} marked
# @return {Integer}
def minimum_distance(n, edges, s, marked)
  g = Array.new(n) { [] }
  edges.each { |u, v, w| g[u] << [v, w] }
  mark = marked.to_h { |x| [x, true] }
  dist = Array.new(n, 10**18)
  dist[s] = 0
  pq = [[0, s]]
  until pq.empty?
    pq.sort_by! { |d, _| d }
    d, u = pq.shift
    return d if mark[u]
    next if d > dist[u]
    g[u].each do |v, w|
      if d + w < dist[v]
        dist[v] = d + w
        pq << [dist[v], v]
      end
    end
  end
  -1
end
