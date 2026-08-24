# LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class UnionFind3600
  attr_reader :cnt

  def initialize(n)
    @p = (0...n).to_a
    @size = Array.new(n, 1)
    @cnt = n
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
    @cnt -= 1
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def max_stability(n, edges, k)
  check = lambda do |lim|
    uf = UnionFind3600.new(n)
    edges.each { |e| uf.unite(e[0], e[1]) if e[2] >= lim }
    rem = k
    edges.each do |e|
      if e[2] * 2 >= lim && rem > 0
        rem -= 1 if uf.unite(e[0], e[1])
      end
    end
    uf.cnt == 1
  end
  uf = UnionFind3600.new(n)
  mn = 1000000
  edges.each do |e|
    if e[3] == 1
      mn = [mn, e[2]].min
      return -1 unless uf.unite(e[0], e[1])
    end
  end
  edges.each { |e| uf.unite(e[0], e[1]) }
  return -1 if uf.cnt > 1
  l = 1
  r = mn
  while l < r
    mid = (l + r + 1) >> 1
    if check.call(mid)
      l = mid
    else
      r = mid - 1
    end
  end
  l
end
