# LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
# https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

class MinCostHeap
  def initialize
    @a = []
  end

  def size
    @a.length
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def up(i)
    a = @a
    while i > 0
      p = (i - 1) >> 1
      break if a[i][0] >= a[p][0]
      a[i], a[p] = a[p], a[i]
      i = p
    end
  end

  def down(i)
    a = @a
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l][0] < a[s][0]
      s = r if r < n && a[r][0] < a[s][0]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_cost_excluding_max(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    u, v, w = e[0], e[1], e[2]
    g[u] << [v, w]
    g[v] << [u, w]
  end
  inf = 10**18
  dist = Array.new(n) { [inf, inf] }
  dist[0][0] = 0
  pq = MinCostHeap.new
  pq.push([0, 0, 0])
  while pq.size > 0
    c, u, used = pq.pop
    next if c > dist[u][used]
    return c if u == n - 1 && used == 1
    g[u].each do |v, w|
      nxt = c + w
      if nxt < dist[v][used]
        dist[v][used] = nxt
        pq.push([nxt, v, used])
      end
      if used == 0
        nxt = c
        if nxt < dist[v][1]
          dist[v][1] = nxt
          pq.push([nxt, v, 1])
        end
      end
    end
  end
  dist[n - 1][1]
end
