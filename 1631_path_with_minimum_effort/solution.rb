# LeetCode 1631 - Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/

class MinHeap1631
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if (@a[p] <=> @a[i]) <= 0

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
    loop do
      l = 2 * i + 1
      r = l + 1
      smallest = i
      smallest = l if l < @a.length && (@a[l] <=> @a[smallest]) < 0
      smallest = r if r < @a.length && (@a[r] <=> @a[smallest]) < 0
      break if smallest == i

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer[][]} heights
# @return {Integer}
def minimum_effort_path(heights)
  m = heights.length
  n = heights[0].length
  dist = Array.new(m) { Array.new(n, Float::INFINITY) }
  dist[0][0] = 0
  heap = MinHeap1631.new
  heap.push([0, 0, 0])
  until heap.empty?
    effort, i, j = heap.pop
    return effort if i == m - 1 && j == n - 1
    next if effort != dist[i][j]

    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |di, dj|
      x = i + di
      y = j + dj
      next unless x.between?(0, m - 1) && y.between?(0, n - 1)

      nd = [effort, (heights[i][j] - heights[x][y]).abs].max
      if nd < dist[x][y]
        dist[x][y] = nd
        heap.push([nd, x, y])
      end
    end
  end
end
