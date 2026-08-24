# LeetCode 0695 - Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
  m = grid.length
  n = grid[0].length

  dfs = lambda do |r, c|
    return 0 if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0

    grid[r][c] = 0
    1 + dfs.call(r + 1, c) + dfs.call(r - 1, c) + dfs.call(r, c + 1) + dfs.call(r, c - 1)
  end

  best = 0
  m.times do |i|
    n.times do |j|
      best = [best, dfs.call(i, j)].max
    end
  end
  best
end
