# LeetCode 3807 - Minimum Cost to Repair Edges to Traverse a Graph
# https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_cost(n, edges, k)
  edges = edges.sort_by { |e| e[2] }
  m = edges.length
  return -1 if m == 0
  check = lambda do |idx|
    g = Array.new(n) { [] }
    (0..idx).each do |i|
      g[edges[i][0]] << edges[i][1]
      g[edges[i][1]] << edges[i][0]
    end
    q = [0]
    vis = Array.new(n, false)
    vis[0] = true
    dist = 0
    while !q.empty?
      nq = []
      q.each do |u|
        return dist <= k if u == n - 1
        g[u].each do |v|
          unless vis[v]
            vis[v] = true
            nq << v
          end
        end
      end
      q = nq
      dist += 1
    end
    false
  end
  l = 0
  r = m - 1
  while l < r
    mid = (l + r) >> 1
    if check.call(mid)
      r = mid
    else
      l = mid + 1
    end
  end
  return edges[l][2] if check.call(l)
  -1
end
