# LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class MinHeap
  def initialize(arr = [])
    @a = arr.dup
    ((@a.length / 2) - 1).downto(0) { |i| down(i) }
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def peek
    @a[0]
  end

  def empty?
    @a.empty?
  end

  def length
    @a.length
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if (@a[i] <=> @a[p]) >= 0

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
      s = l if l < n && (@a[l] <=> @a[s]) < 0
      s = r if r < n && (@a[r] <=> @a[s]) < 0
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[][]} grid
# @return {Integer}
def minimum_time(grid)
  return -1 if grid[0][1] > 1 && grid[1][0] > 1

  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, 1 << 30) }
  h = MinHeap.new
  h.push([0, 0, 0])
  dist[0][0] = 0
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  until h.empty?
    t, r, c = h.pop
    return t if r == m - 1 && c == n - 1
    next if t > dist[r][c]

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n

      nt = t + 1
      if nt < grid[nr][nc]
        wait = grid[nr][nc] - nt
        wait += 1 if wait.odd?
        nt += wait
      end
      if nt < dist[nr][nc]
        dist[nr][nc] = nt
        h.push([nt, nr, nc])
      end
    end
  end
  -1
end
