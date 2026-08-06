# LeetCode 1368 - Minimum Cost To Make At Least One Valid Path In A Grid
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

def min_cost(grid)
  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, 10**9) }
  dist[0][0] = 0
  q = [[0, 0]]
  dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  until q.empty?
    r, c = q.shift
    dirs.each_with_index do |(dr, dc), idx|
      k = idx + 1
      x = r + dr
      y = c + dc
      next unless x >= 0 && x < m && y >= 0 && y < n
      w = k != grid[r][c] ? 1 : 0
      nd = dist[r][c] + w
      next unless nd < dist[x][y]
      dist[x][y] = nd
      w == 1 ? q.push([x, y]) : q.unshift([x, y])
    end
  end
  dist[-1][-1]
end
