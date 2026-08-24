# LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class MinHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?

    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def size
    @a.length
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i][0] >= @a[p][0]

      @a[i], @a[p] = @a[p], @a[i]
      i = p
    end
  end

  def down(i)
    n = @a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && @a[l][0] < @a[s][0]
      s = r if r < n && @a[r][0] < @a[s][0]
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} src1
# @param {Integer} src2
# @param {Integer} dest
# @return {Integer}
def minimum_weight(n, edges, src1, src2, dest)
  inf = (1 << 53) - 1

  dijkstra = lambda do |g, src|
    dist = Array.new(n, inf)
    dist[src] = 0
    pq = MinHeap.new
    pq.push([0, src])
    while pq.size > 0
      d, u = pq.pop
      next if d != dist[u]

      g[u].each do |v, w|
        if d + w < dist[v]
          dist[v] = d + w
          pq.push([dist[v], v])
        end
      end
    end
    dist
  end

  g = Array.new(n) { [] }
  rg = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    rg[e[1]] << [e[0], e[2]]
  end
  d1 = dijkstra.call(g, src1)
  d2 = dijkstra.call(g, src2)
  dd = dijkstra.call(rg, dest)
  ans = inf
  n.times do |i|
    next if d1[i] >= inf || d2[i] >= inf || dd[i] >= inf

    ans = [ans, d1[i] + d2[i] + dd[i]].min
  end
  ans >= inf ? -1 : ans
end
