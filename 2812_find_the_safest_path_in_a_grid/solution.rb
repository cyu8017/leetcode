# LeetCode 2812 - Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def maximum_safeness_factor(grid)
  n = grid.length
  dist = Array.new(n) { Array.new(n, -1) }
  q = []
  (0...n).each do |i|
    (0...n).each do |j|
      if grid[i][j] == 1
        dist[i][j] = 0
        q << [i, j]
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  h = 0
  while h < q.length
    x, y = q[h]
    h += 1
    dirs.each do |dx, dy|
      ni = x + dx
      nj = y + dy
      if ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1
        dist[ni][nj] = dist[x][y] + 1
        q << [ni, nj]
      end
    end
  end

  ok = lambda do |sf|
    return false if dist[0][0] < sf
    seen = Array.new(n) { Array.new(n, false) }
    st = [[0, 0]]
    seen[0][0] = true
    until st.empty?
      x, y = st.pop
      return true if x == n - 1 && y == n - 1
      dirs.each do |dx, dy|
        ni = x + dx
        nj = y + dy
        if ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf
          seen[ni][nj] = true
          st << [ni, nj]
        end
      end
    end
    false
  end

  lo = 0
  hi = n * n
  ans = 0
  while lo <= hi
    mid = (lo + hi) >> 1
    if ok.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
