# LeetCode 2093 - Minimum Cost to Reach City With Discounts
# https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

class MinHeap2093
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i > 0
      p = (i - 1) / 2
      break if @a[p] <= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    n = @a.length
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= n

      smallest = r < n && @a[r] < @a[l] ? r : l
      break if @a[i] <= @a[smallest]

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer} n
# @param {Integer[][]} highways
# @param {Integer} discounts
# @return {Integer}
def minimum_cost(n, highways, discounts)
  g = Array.new(n) { [] }
  highways.each do |a, b, c|
    g[a] << [b, c]
    g[b] << [a, c]
  end
  inf = 1 << 30
  dist = Array.new(n) { Array.new(discounts + 1, inf) }
  dist[0][discounts] = 0
  pq = MinHeap2093.new
  pq.push([0, 0, discounts])
  until pq.empty?
    cost, city, disc = pq.pop
    return cost if city == n - 1
    next if cost > dist[city][disc]

    g[city].each do |v, w|
      if cost + w < dist[v][disc]
        dist[v][disc] = cost + w
        pq.push([dist[v][disc], v, disc])
      end
      if disc > 0 && cost + w / 2 < dist[v][disc - 1]
        dist[v][disc - 1] = cost + w / 2
        pq.push([dist[v][disc - 1], v, disc - 1])
      end
    end
  end
  -1
end
