# LeetCode 1697 - Checking Existence of Edge Length Limited Paths
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

# @param {Integer} n
# @param {Integer[][]} edge_list
# @param {Integer[][]} queries
# @return {Boolean[]}
def distance_limited_paths_exist(n, edge_list, queries)
  parent = (0...n).to_a
  find = lambda do |x|
    while x != parent[x]
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  ans = Array.new(queries.length, false)
  edges = edge_list.sort_by { |e| e[2] }
  i = 0
  queries.each_with_index.map { |(a, b, lim), j| [lim, a, b, j] }.sort.each do |limit, p, q, idx|
    while i < edges.length && edges[i][2] < limit
      a, b, = edges[i]
      parent[find.call(a)] = find.call(b)
      i += 1
    end
    ans[idx] = find.call(p) == find.call(q)
  end
  ans
end
