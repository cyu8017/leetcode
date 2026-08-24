# LeetCode 3108 - Minimum Cost Walk in Weighted Graph
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} query
# @return {Integer[]}
def minimum_cost(n, edges, query)
  p = (0...n).to_a
  size = Array.new(n, 1)

  find = lambda do |x|
    p[x] = find.call(p[x]) if p[x] != x
    p[x]
  end

  unite = lambda do |a, b|
    pa = find.call(a)
    pb = find.call(b)
    return if pa == pb
    if size[pa] > size[pb]
      p[pb] = pa
      size[pa] += size[pb]
    else
      p[pa] = pb
      size[pb] += size[pa]
    end
  end

  g = Array.new(n, -1)
  edges.each { |e| unite.call(e[0], e[1]) }
  edges.each do |e|
    root = find.call(e[0])
    g[root] &= e[2]
  end
  query.map do |u, v|
    if u == v
      0
    else
      a = find.call(u)
      b = find.call(v)
      a == b ? g[a] : -1
    end
  end
end
