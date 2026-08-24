# LeetCode 0980 - Unique Paths III
# https://leetcode.com/problems/unique-paths-iii/

# @param {Integer[][]} grid
# @return {Integer}
def unique_paths_iii(grid)
  m = grid.length
  n = grid[0].length
  empty = 0
  sr = sc = 0
  m.times do |i|
    n.times do |j|
      empty += 1 if grid[i][j] != -1
      if grid[i][j] == 1
        sr = i
        sc = j
      end
    end
  end
  ans = 0

  dfs = lambda do |r, c, remain|
    if grid[r][c] == 2
      ans += 1 if remain == 1
      return
    end
    temp = grid[r][c]
    grid[r][c] = -1
    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      dfs.call(nr, nc, remain - 1) if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1
    end
    grid[r][c] = temp
  end

  dfs.call(sr, sc, empty)
  ans
end
