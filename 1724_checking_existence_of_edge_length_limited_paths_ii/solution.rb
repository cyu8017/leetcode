# LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

class DistanceLimitedPathsExist
  # @param {Integer} n
  # @param {Integer[][]} edge_list
  def initialize(n, edge_list)
    edges = edge_list.map { |u, v, w| [w, u, v] }.sort
    @weights = []
    @versions = []
    parent = (0...n).to_a
    size = Array.new(n, 1)
    find = lambda do |x|
      while parent[x] != x
        parent[x] = parent[parent[x]]
        x = parent[x]
      end
      x
    end
    i = 0
    while i < edges.length
      weight = edges[i][0]
      while i < edges.length && edges[i][0] == weight
        ra = find.call(edges[i][1])
        rb = find.call(edges[i][2])
        if ra != rb
          ra, rb = rb, ra if size[ra] < size[rb]
          parent[rb] = ra
          size[ra] += size[rb]
        end
        i += 1
      end
      @weights << weight
      @versions << parent.dup
    end
  end

  # @param {Integer} p
  # @param {Integer} q
  # @param {Integer} limit
  # @return {Boolean}
  def query(p, q, limit)
    idx = @weights.bsearch_index { |w| w >= limit } || @weights.length
    idx -= 1
    return p == q if idx < 0
    parent = @versions[idx]
    rp = p
    rp = parent[rp] while parent[rp] != rp
    rq = q
    rq = parent[rq] while parent[rq] != rq
    rp == rq
  end
end
