# LeetCode 1219 - Path with Maximum Gold
# https://leetcode.com/problems/path-with-maximum-gold/

# @param {Integer[][]} grid
# @return {Integer}
def get_maximum_gold(grid)
  rows = grid.length
  cols = grid[0].length
  dfs = nil
  dfs = lambda do |r, c|
    gold = grid[r][c]
    grid[r][c] = 0
    best = 0
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      nr = r + dr
      nc = c + dc
      if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != 0
        best = [best, dfs.call(nr, nc)].max
      end
    end
    grid[r][c] = gold
    gold + best
  end
  ans = 0
  rows.times { |r| cols.times { |c| ans = [ans, dfs.call(r, c)].max if grid[r][c] != 0 } }
  ans
end
