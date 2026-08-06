# LeetCode 1559 - Detect Cycles in 2D Grid
# https://leetcode.com/problems/detect-cycles-in-2d-grid/

# @param {Character[][]} grid
# @return {Boolean}
def contains_cycle(grid)
  m = grid.length
  n = grid[0].length
  seen = {}
  dfs = lambda do |r, c, pr, pc|
    seen[[r, c]] = true
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)
      next if grid[nr][nc] != grid[r][c] || (nr == pr && nc == pc)
      return true if seen[[nr, nc]] || dfs.call(nr, nc, r, c)
    end
    false
  end
  (0...m).any? do |r|
    (0...n).any? { |c| !seen[[r, c]] && dfs.call(r, c, -1, -1) }
  end
end
