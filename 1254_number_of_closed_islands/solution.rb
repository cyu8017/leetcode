# LeetCode 1254 - Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/

# @param {Integer[][]} grid
# @return {Integer}
def closed_island(grid)
  m = grid.length
  n = grid[0].length
  flood = lambda do |sr, sc|
    stack = [[sr, sc]]
    closed = true
    grid[sr][sc] = 1
    until stack.empty?
      r, c = stack.pop
      closed = false if r == 0 || r == m - 1 || c == 0 || c == n - 1
      [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
        nr = r + dr
        nc = c + dc
        if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0
          grid[nr][nc] = 1
          stack << [nr, nc]
        end
      end
    end
    closed
  end
  ans = 0
  m.times { |r| n.times { |c| ans += 1 if grid[r][c] == 0 && flood.call(r, c) } }
  ans
end
