# LeetCode 3608 - Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components/

class UnionFind3608
  def initialize(n)
    @p = (0...n).to_a
    @size = Array.new(n, 1)
  end

  def find(x)
    @p[x] = find(@p[x]) if @p[x] != x
    @p[x]
  end

  def unite(a, b)
    pa = find(a)
    pb = find(b)
    return false if pa == pb
    if @size[pa] > @size[pb]
      @p[pb] = pa
      @size[pa] += @size[pb]
    else
      @p[pa] = pb
      @size[pb] += @size[pa]
    end
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_time(n, edges, k)
  edges = edges.sort_by { |e| e[2] }
  uf = UnionFind3608.new(n)
  cnt = n
  (edges.length - 1).downto(0) do |i|
    if uf.unite(edges[i][0], edges[i][1])
      cnt -= 1
      return edges[i][2] if cnt < k
    end
  end
  0
end
