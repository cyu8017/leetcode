# LeetCode 1627 - Graph Connectivity With Threshold
# https://leetcode.com/problems/graph-connectivity-with-threshold/

# @param {Integer} n
# @param {Integer} threshold
# @param {Integer[][]} queries
# @return {Boolean[]}
def are_connected(n, threshold, queries)
  parent = (0..n).to_a
  find = lambda do |x|
    while x != parent[x]
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  ((threshold + 1)..n).each do |d|
    (2 * d).step(n, d) do |x|
      a = find.call(d)
      b = find.call(x)
      parent[b] = a if a != b
    end
  end
  queries.map { |a, b| find.call(a) == find.call(b) }
end
