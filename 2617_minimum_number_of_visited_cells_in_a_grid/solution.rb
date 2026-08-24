# LeetCode 2617 - Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_visited_cells(grid)
  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, -1) }
  q = [[0, 0]]
  dist[0][0] = 1
  until q.empty?
    r, c = q.shift
    return dist[r][c] if r == m - 1 && c == n - 1

    nc = c + 1
    while nc <= c + grid[r][c] && nc < n
      if dist[r][nc] == -1
        dist[r][nc] = dist[r][c] + 1
        q << [r, nc]
      end
      nc += 1
    end
    nr = r + 1
    while nr <= r + grid[r][c] && nr < m
      if dist[nr][c] == -1
        dist[nr][c] = dist[r][c] + 1
        q << [nr, c]
      end
      nr += 1
    end
  end
  -1
end
