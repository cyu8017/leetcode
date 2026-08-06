# LeetCode 1391 - Check If There Is A Valid Path In A Grid
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

def has_valid_path(grid)
  dirs = {
    1 => [[0, -1], [0, 1]],
    2 => [[-1, 0], [1, 0]],
    3 => [[0, -1], [1, 0]],
    4 => [[0, 1], [1, 0]],
    5 => [[0, -1], [-1, 0]],
    6 => [[0, 1], [-1, 0]]
  }
  m = grid.length
  n = grid[0].length
  seen = { [0, 0] => true }
  st = [[0, 0]]
  until st.empty?
    r, c = st.pop
    return true if [r, c] == [m - 1, n - 1]
    dirs[grid[r][c]].each do |dr, dc|
      x = r + dr
      y = c + dc
      next unless x >= 0 && x < m && y >= 0 && y < n && !seen[[x, y]]
      next unless dirs[grid[x][y]].include?([-dr, -dc])
      seen[[x, y]] = true
      st << [x, y]
    end
  end
  false
end
