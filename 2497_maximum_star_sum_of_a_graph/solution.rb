# LeetCode 2497 - Maximum Star Sum of a Graph
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

# @param {Integer[]} vals
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def max_star_sum(vals, edges, k)
  n = vals.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  ans = vals[0]
  (0...n).each do |i|
    neigh = []
    g[i].each { |v| neigh << vals[v] if vals[v] > 0 }
    neigh.sort!.reverse!
    s = vals[i]
    [neigh.length, k].min.times { |j| s += neigh[j] }
    ans = s if s > ans
  end
  ans
end
