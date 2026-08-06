# LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Dsu
  attr_reader :components

  def initialize(n)
    @parent = (0..n).to_a
    @components = n
  end

  def find(x)
    while x != @parent[x]
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(a, b)
    a = find(a)
    b = find(b)
    return false if a == b
    @parent[a] = b
    @components -= 1
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def max_num_edges_to_remove(n, edges)
  alice = Dsu.new(n)
  bob = Dsu.new(n)
  used = 0
  edges.each do |t, u, v|
    next unless t == 3
    merged = alice.union(u, v)
    bob.union(u, v)
    used += 1 if merged
  end
  edges.each do |t, u, v|
    if t == 1
      used += 1 if alice.union(u, v)
    elsif t == 2
      used += 1 if bob.union(u, v)
    end
  end
  alice.components == 1 && bob.components == 1 ? edges.length - used : -1
end
