# LeetCode 2658 - Maximum Number of Fish in a Grid
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def find_max_fish(grid)
  m = grid.length
  n = grid[0].length
  dfs = nil
  dfs = lambda do |r, c|
    return 0 if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0

    fish = grid[r][c]
    grid[r][c] = 0
    fish + dfs.call(r + 1, c) + dfs.call(r - 1, c) + dfs.call(r, c + 1) + dfs.call(r, c - 1)
  end
  best = 0
  m.times do |i|
    n.times do |j|
      best = [best, dfs.call(i, j)].max if grid[i][j] > 0
    end
  end
  best
end
